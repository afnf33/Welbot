from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest.serializers import *
from rest.models import *
import pandas as pd
import os
from logging import DEBUG, getLogger
from dialogflow_fulfillment import WebhookClient
from django.views.decorators.csrf import csrf_exempt
import json

module_dir = os.path.dirname(__file__)
LOG = getLogger(__name__)
LOG.setLevel(DEBUG)

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

class InfraViewSet(viewsets.ModelViewSet):
    queryset = Infrastructure.objects.all()
    serializer_class = InfraSerializer
    permission_classes = [permissions.IsAuthenticated]
#복지시설
class WelFacilityViewSet(viewsets.ModelViewSet):
    queryset = Wel_facility.objects.all()
    serializer_class = WelFacilitySerializer
    permission_classes = [permissions.IsAuthenticated]

class SeniorCenterViewSet(viewsets.ModelViewSet):
    queryset = Senior_center.objects.all()
    serializer_class = SeniorCenterSerializer
    permission_classes = [permissions.IsAuthenticated]
#교육시설
class EduViewSet(viewsets.ModelViewSet):
    queryset = Edu_facility.objects.all()
    serializer_class = EduSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LectureGenreViewSet(viewsets.ModelViewSet):
    queryset = Lecture_Genre.objects.all()
    serializer_class = LectureGenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AcademyViewSet(viewsets.ModelViewSet):
    queryset = Academy.objects.all()
    serializer_class = AcademySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AcademyLectureViewSet(viewsets.ModelViewSet):
    queryset = Academy_lecture.objects.all()
    serializer_class = AcademyLectureSerializer
    permission_classes = [permissions.IsAuthenticated]
#두드림길
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseTypeViewSet(viewsets.ModelViewSet):
    queryset = Course_type.objects.all()
    serializer_class = CourseTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CoursePointViewSet(viewsets.ModelViewSet):
    queryset = Course_point.objects.all()
    serializer_class = CoursePointSerializer
    permission_classes = [permissions.IsAuthenticated]
#문화행사    
class CultureGenreViewSet(viewsets.ModelViewSet):
    queryset = Culture_genre.objects.all()
    serializer_class = CultureGenreSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CultureEventViewSet(viewsets.ModelViewSet):
    queryset = Culture_Event.objects.all()
    serializer_class = CultureEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    

def index(request):    
    return HttpResponse("index page!")
    
    
def city_init(request):
    city_bulk = []
    cities = ['강남구', '강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
    for i, value in enumerate(cities):
        data = City(city_id=(i+1), name=value)
        city_bulk.append(data)
        
    City.objects.bulk_create(city_bulk)
    
    return HttpResponse('City initialized!')

def infra_init(request):
    infra_bulk = []
    infra = ['복지시설', '경로당','교육시설','두드림길','문화행사']
    for i, value in enumerate(infra):
        data = Infrastructure(infra_id = (i+1), name = value)
        infra_bulk.append(data)
    
    Infrastructure.objects.bulk_create(infra_bulk)
    
    return HttpResponse("Infra initialized!")


def edu_init(request):
    edu_fac_bulk = []
    edu = ['노인교실', '평생학습포털']
    for i, value in enumerate(edu):
        data = Edu_facility(id = (i+1), name = value, kind = Infrastructure.objects.get(name='교육시설'))
        edu_fac_bulk.append(data)
        
    Edu_facility.objects.bulk_create(edu_fac_bulk)
    
    return HttpResponse('Edu_facility initialized!')

def course_type(request):
    type_bulk = []
    type = ['생태문화길', '서울둘레길','근교산자락길', '한양도성길', '한강지천길(계절길)']
    for i, value in enumerate(type):
        data = Course_type(id = (i+1), name=value, code = (i+1)*1000)
        type_bulk.append(data)
        
    Course_type.objects.bulk_create(type_bulk)
    
    return HttpResponse('Course_type initialized!')


def senior_center_init(request):
    sc_bulk = []
    path = os.path.join(module_dir, 'templates/rest/files/경로당/')
    file_1 = '서울특별시 경로당 정보(20180502).xlsx'
    file_2 = '서울시 강북구 경로당 현황.csv'
    df = pd.read_excel(path+file_1)
    df2 = pd.read_csv(path+file_2, encoding='cp949')
    
    df = df.loc(axis=1)[['사업장명','소재지전체주소']]
    df.columns = ['name','address']
    
    raw_address = df['address'].values
    print(raw_address[:5])
    city = []
    for x in raw_address:
        city.append(x.split()[1])
    print(city[:5])
    df['city'] = city
    
    address = []
    for x in raw_address:
        address.append(x[6:])
    df['address'] = address
    
    df_ = df[df['city'] == '강북구'].index
    df.drop(df_, inplace=True)
    
    df2 = df2.loc(axis=1)[['경로당명', '도로명 주소', '전 화']]
    df2.columns = ['name','address','tel']
    
    name = []
    for x in df2['name'].values:
        if x[:-1] != '당':
            name.append(x+'경로당')
        
    df2['name'] = name
    
    df_c = pd.concat([df, df2])
    df_c['city'].fillna('강북구', inplace=True)
    df_c['tel'].fillna('없음', inplace=True)
    
    df_c.to_csv('경로당.csv', encoding='utf8')
    for i, sc in enumerate(df_c.values):
        data = Senior_center(id = (i+1), 
                             name = sc[0], 
                             kind = Infrastructure.objects.get(name='경로당'), 
                             city = City.objects.get(name=sc[2]), 
                             address = sc[1], 
                             tel = sc[3])
        sc_bulk.append(data)
    
    Senior_center.objects.bulk_create(sc_bulk)
    
    return HttpResponse('Senior_center initialized!')


def wel_facility_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/복지시설/')
    file = '서울시 어르신 복지시설 현황.csv'
    city_bulk = []
    
    df = pd.read_csv(path+file, encoding='cp949')
    
    df = df.loc(axis=1)[['자치구','시설명','신주소']]
    df.columns = ['city', 'name', 'address']
    
    city = []
    raw_city = df['city'].values
    for x in raw_city:
        city.append(x+'구')
    df['city'] = city
    
    for i, wf in enumerate(df.values):
        data = Wel_facility(id = (i+1),
                            name = wf[1],
                            kind = Infrastructure.objects.get(name='복지시설'),
                            city = City.objects.get(name=wf[0]),
                            address = wf[2])
        city_bulk.append(data)
        
    Wel_facility.objects.bulk_create(city_bulk)
    
    return HttpResponse('Wel_facility initialized!')
    

def school_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/노인교실/')
    file_1 = '서울특별시 노인교실 정보_20180821.csv'
    file_2 = '서울시 강북구 노인교실 현황.csv'
    
    df = pd.read_csv(path+file_1, encoding='cp949')
    df2 = pd.read_csv(path+file_2, encoding='cp949')
    
    df = df.loc(axis=1)[['사업장명','소재지전체주소']]
    df.columns = ['name','address']
    df = df.drop_duplicates()
    
    raw_address = df['address'].values
    address = []
    city = []
    for val in raw_address:
        address.append(val[6:])
        city.append(val.split()[1])
    df['address'] = address
    df['city'] = city
    
    idx = df[df['city'] == '강북구'].index
    df.drop(idx, inplace=True)
    
    df2 = df2.loc(axis=1)[['노인교실명','소재지','전화번호']]
    df2.columns = ['name','address','tel']
    
    df = pd.concat([df, df2])
    df['city'] = df['city'].fillna('강북구')
    df['tel'] = df['tel'].fillna('없음')
    
    school_bulk = []
    for i, val in enumerate(df.values):
        data = School(id = (i+1),
                      name = val[0],
                      kind = Edu_facility.objects.get(name='노인교실'),
                      city = City.objects.get(name=val[2]),
                      address = val[1],
                      tel = val[3])
        school_bulk.append(data)
        
    School.objects.bulk_create(school_bulk)
    
    return HttpResponse('School initialized!')


def lecture_init(request):
    type = ['온라인', '오프라인']
    genre = ['예술', '언어', '체육', '요리', '신기술','기타' '자기계발']
    
    type_bulk = []
    genre_bulk = []
    for i, val in enumerate(type):
        data = Lecture(id = (i+1), name = val)
        type_bulk.append(data)
        
        
    for i, val in enumerate(genre):
        data = Lecture_Genre(id = (i+1),name = val)
        genre_bulk.append(data)
    
    Lecture.objects.bulk_create(type_bulk)
    Lecture_Genre.objects.bulk_create(genre_bulk)
    
    return HttpResponse('Lecture initialized!')

def academy_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/평생교육/')
    file = '서울시 평생학습포털 평생교육기관 현황.csv'
    
    df = pd.read_csv(path+file, encoding='cp949')
    
    df.drop(['위치(위도)','위치(경도)'], axis=1, inplace=True)
    df.columns = ['name','tel','address','url']
    df.drop(df[df['address'].isnull()].index, inplace=True)
    df.fillna('없음', inplace=True)
    
    df.drop_duplicates(inplace=True)
    df = df.drop_duplicates(['name'], keep='last')
    df = df.drop_duplicates(['address'], keep='last')
    
    raw_address = df['address'].values
    city = []
    found = False
    index = []
    drop_ = []
    for idx, data in enumerate(raw_address):
        tmp = data.split()
        for val in tmp:
            found = False
            if '없음' in val:
                city.append('없음')
                found = True
            elif '경기' in val:
                drop_.append(idx)
                break
            elif '구' in val:
                if val == '구로구':
                    city.append(val)
                else :
                    idx = val.find('구')
                    city.append(val[:idx+1])
                found = True
                break
        if not found:
            index.append(idx)
            city.append('*')
    cities = ['금천구', '강남구','강남구','강남구','강남구','강남구','강남구','강남구',
              '강남구','강남구','강남구','관악구','성동구','영등포구','관악구', '서초구','도봉구','영등포구','노원구','종로구','성동구','용산구','중구','*']
    
    df['city'] = city
    df = df.reset_index()
    df.drop('index', axis=1, inplace=True)
    df.drop(drop_, inplace=True)
    df[df['city']=='*']['city'] = cities
    df.drop(df[df['city'] == '*'].index, inplace=True)
    
    df = df.reset_index()
    df.drop('index',axis=1, inplace=True)
    idx = df[df['city'] == '구'].index
    df.iloc[idx[0]]['city'] = '구로구'
    df.drop(idx[1], inplace=True)
    confirm = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']
    invalid = []
    for val in df['city']:
        if val not in confirm:
            invalid.append(val)
    
    aca_bulk = []
    for i, val in enumerate(df.values):
        try :
            data = Academy(id = (i+1),
                       name = val[0],
                       kind = Edu_facility.objects.get(name='평생학습포털'),
                       city = City.objects.get(name = val[4]),
                       tel = val[1],
                       address = val[2],
                       url = val[3])
            aca_bulk.append(data)
        except:
            continue
        
        
    Academy.objects.bulk_create(aca_bulk)
    
    return HttpResponse('Academy initialized!')

def academy_preprocess():
    path = os.path.join(module_dir, 'templates/rest/files/평생교육/')
    file_1 = '서울시 평생학습포털 사이버강의 정보.csv'
    file_2 = '서울시 평생학습포털 오프라인강좌 정보.csv'
    
    df = pd.read_csv(path+file_1, encoding='cp949')
    df.drop(['강좌목차번호','강좌목차', '교육시작일', '교육종료일','정원'], axis=1, inplace=True)
    df.drop_duplicates(inplace = True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    df.columns = ['code', 'name', 'type', 'startdate', 'enddate', 'target', 'level', 'url']
    df.fillna('없음', inplace=True)
    
    start = []
    end = []
    for i in range(len(df['startdate'].values)):
        try:
            tmp1 = str(int(df['startdate'].values[i]))
            tmp2 = str(int(df['enddate'].values[i]))
            start.append(tmp1[:4]+'/'+tmp1[4:6]+'/'+tmp1[6:8])
            end.append(tmp2[:4]+'/'+tmp2[4:6]+'/'+tmp2[6:8])
        except:
            start.append('없음')
            end.append('없음')
            continue
    
    df.loc(axis=1)['startdate'] = start
    df.loc(axis=1)['enddate'] = end
    
    df2 = pd.read_csv(path+file_2, encoding='cp949')
    df2.drop_duplicates(inplace=True)
    df2.drop(['교육시작일', '교육종료일', '정원'], axis=1, inplace=True)
    df2.columns = ['code','name','type', 'startdate', 'enddate', 'target', 'url']
    df2.fillna('없음', inplace=True)
    
    start = []
    end = []
    for i in range(len(df2['startdate'].values)):
        tmp1 = str(int(df2['startdate'].values[i]))
        tmp2 = str(int(df2['enddate'].values[i]))
        start.append(tmp1[:4]+'/'+tmp1[4:6]+'/'+tmp1[6:8])
        end.append(tmp2[:4]+'/'+tmp2[4:6]+'/'+tmp2[6:8])
    
    df2.loc(axis=1)['startdate'] = start
    df2.loc(axis=1)['enddate'] = end
    
    df_ = pd.concat([df, df2])
    df_.fillna('없음', inplace=True)
    
    df_.to_csv('lecture.csv')
    
def academy_lect_init(request):
    #academy_preprocess()
    path = os.path.join(module_dir, 'templates/rest/files/평생교육/')
    file = 'lecture_preprocessed.csv'
    
    df = pd.read_csv(path+file, encoding='cp949')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    
    lect_bulk = []
    for i, val in enumerate(df.values):
        s_date = None if val[4] == '없음' else val[4]
        e_date = None if val[5] == '없음' else val[5]
        data = Academy_lecture(id = (i+1),
                               name =  val[2],
                               code = val[1],
                               type = Lecture.objects.get(name = val[3]),
                               genre = Lecture_Genre.objects.get(name = val[0]),
                               target = val[6],
                               level = val[7],
                               startdate = s_date,
                               enddate = e_date,
                               url = val[8])
        lect_bulk.append(data)
    Academy_lecture.objects.bulk_create(lect_bulk)
    
    return HttpResponse('Academy_lecture initialized!')

def course_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/두드림길/')
    file = '서울 두드림길 정보.csv'
    
    df = pd.read_csv(path+file, encoding='cp949')
    df1 = df.loc(axis=1)['코스 카테고리', '코스명', '거리', '소요시간', '코스레벨','자치구', '설명','PDF파일경로']
    df1.columns = ['type', 'name', 'length', 'time', 'level', 'city', 'desc', 'url']
    df1.fillna('없음', inplace=True)
    df1.drop_duplicates(inplace=True)
    df1['city'].replace('없음', '송파구', inplace = True)
    
    df2 = df.loc(axis=1)['코스명', '포인트명칭', '포인트 설명']
    df2.columns = ['name', 'course', 'desc']
    
    course_bulk = []
    point_bulk = []
    
    for i, val in enumerate(df1.values):
        tmp = val[5].split('구')
        cities = []
        for ct in tmp:
            if ct == '로':
                cities.append('구로구')
            elif ct == '':
                pass
            else :
                cities.append(ct+'구')
        
        data = Course(id = (i+1),
                      name = val[1],
                      type = Course_type.objects.get(code = val[0]),
                      kind = Infrastructure.objects.get(name = '두드림길'),
                      city = cities,
                      level = val[4],
                      time = val[3],
                      desc = val[6],
                      url = val[7]
                      )
        course_bulk.append(data)
        
    Course.objects.bulk_create(course_bulk)
    
    
    for i, val in enumerate(df2.values):
        data = Course_point(id = (i+1),
                            name = val[1],
                            course = Course.objects.get(name = val[0]),
                            desc= val[2])
        point_bulk.append(data)
        
    Course_point.objects.bulk_create(point_bulk)
    
    return HttpResponse('Course initialized!')



def culture_genre_init(request):
    genre = ['클래식', '뮤지컬_오페라', '전시회', '연극', '콘서트', '국악', '무용', '전시_관람']
    genre_bulk = []
    
    for i, val in enumerate(genre):
        data = Culture_genre(id = (i+1),
                             name = val)
        genre_bulk.append(data)
        
    Culture_genre.objects.bulk_create(genre_bulk)
    
    return HttpResponse('Culture_Genre initialized!')


def exhibit_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/문화/')
    file = '서울시 문화행사 공공서비스예약 정보.csv'
    
    df = pd.read_csv(path+file, encoding='cp949')
    df = df.loc(axis=1)['대분류명', '소분류명', '서비스명', '장소명', '지역명', '서비스대상', '바로가기URL', '전화번호', '이미지경로', '서비스이용 시작시간', '서비스이용 종료시간']
    df.columns = ['kind', 'genre', 'name', 'location', 'city', 'target', 'url', 'tel', 'image', 'starttime', 'endtime']
    df.fillna('없음', inplace=True)
    
    bulk_data = []
    for i, val in enumerate(df.values):
        data = Exhibition(id = (i+1),
                          name = val[2],
                          location= val[3],
                          city= City.objects.get(name = val[4]),
                          genre = Culture_genre.objects.get(name = '전시_관람'),
                          kind =  Infrastructure.objects.get(name = val[0]),
                          tel = val[7],
                          target = val[5],
                          url = val[6],
                          image = val[8],
                          starttime = val[9],
                          endtime = val[10])
        bulk_data.append(data)
        
    Exhibition.objects.bulk_create(bulk_data)
    
    return HttpResponse('Exhibition initialized!')

def culture_event_init(request):
    path = os.path.join(module_dir, 'templates/rest/files/문화/')
    file = '서울특별시 문화행사 정보.csv'
    
    df = pd.read_csv(path+file, encoding='cp949')
    df = df.loc(axis=1)['분류', '공연/행사명', '날짜/시간', '장소', '기관명', '이용대상', '이용요금', '홈페이지?주소', '대표이미지']
    df.columns = ['genre', 'name', 'date', 'location', 'company', 'target', 'fare', 'url', 'image']
    
    df.fillna('', inplace=True)
    date = df['date'].values
    startdate = []
    enddate = []
    for val in date:
        tmp1, tmp2 = val.split('~')
        startdate.append(tmp1)
        enddate.append(tmp2)
    
    df.drop('date', axis=1, inplace=True)
    df['startdate'] = startdate
    df['enddate'] = enddate
    
    location = df['location'].values
    company = df['company'].values
    result = []
    for i in range(len(location)):
        if company[i] in location[i]:
            result.append(location[i])
        else:
            result.append(company[i] + ' '+ location[i])
    
    df.drop(['location', 'company'], axis=1, inplace=True)
    df['location'] = result
    
    df.drop_duplicates(['name'], keep='last', inplace=True)
    df.replace('&amp;', '&', inplace=True)
    df.replace('&lt;', '<', inplace=True)
    df.replace('&gt;', '>', inplace=True)
    df.replace('&quot;', '"', inplace=True)
    df.replace('&nbsp;', ' ', inplace=True)
    
    event_bulk = []
    for i, val in enumerate(df.values):
        if val[0] == '뮤지컬/오페라' : 
            val[0] = '뮤지컬_오페라' 
        data = Culture_Event(id = (i+1),
                             name = val[1],
                             genre = Culture_genre.objects.get(name = val[0]),
                             kind = Infrastructure.objects.get(name = '문화행사'),
                             startdate = val[6],
                             enddate = val[7],
                             location = val[8],
                             target = val[2],
                             fare = val[3],
                             url = val[4],
                             image = val[5])
        event_bulk.append(data)
        
    Culture_Event.objects.bulk_create(event_bulk)
    
    return HttpResponse('Culture_Event initialized!')

def handler(agent):
    ''' custom handler functions '''
    
    





@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        jsondata = request.body
        data = json.loads(jsondata)
        
        print(data)
        
        '''
        request_ = request.POST.dict()
        print(type(request_))
        for key, val in request_:
            print(key, val)
        print(request_)
        '''
        LOG.info(f'Request headers: {dict(request.headers)}')
        LOG.info(f'Request body: {request_}')
        #LOG.info(f'Response body: {agent.response}')
        
        return JsonResponse(request)










