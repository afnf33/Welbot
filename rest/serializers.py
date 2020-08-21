from rest_framework import serializers
from rest.models import *

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('city_id', 'name')
           
class InfraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Infrastructure
        fields = ('infra_id','name')
#복지시설
class WelFacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wel_facility
        fields = ('id','name','kind', 'city', 'address')

class SeniorCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Senior_center
        fields = ('id','name','kind','city','address','tel')
#교육시설
class EduSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edu_facility
        fields = ('id','name','kind')
            
class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','kind','city','address','tel')
        
class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id','name')

class LectureGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture_Genre
        fields = ('id','name')
        
class AcademySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Academy
        fields = ('id','name','kind','city','address','tel', 'url')

class AcademyLectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Academy_lecture
        fields = ('id','name','code','type','genre','target', 'startdate', 'enddate', 'url')
#두드림길
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name','type', 'kind','city','length', 'time','desc','url')

class CourseTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course_type
        fields = ('id', 'name', 'code')

class CoursePointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course_point
        fields = ('id','name','course', 'desc')
#문화행사
class CultureGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Culture_genre
        fields = ('id','name')
        
class ExhibitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('id','name','available', 'location', 'city','genre', 'kind', 'tel','target','url', 'image','starttime','endtime')

class CultureEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Culture_Event
        fields = ('id','name','genre','kind', 'startdate', 'enddate', 'location','target','fare','available','url','image')


