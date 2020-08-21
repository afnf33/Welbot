from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class City(models.Model):
    city_id = models.IntegerField()
    name = models.CharField(max_length = 5, primary_key=True)
    #city_code = models.IntegerField()

class Infrastructure(models.Model):
    infra_id = models.IntegerField()
    name = models.CharField(max_length = 10, primary_key =True)

#복지시설
class Wel_facility(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=15, primary_key = True)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)
    city = models.ForeignKey(City, on_delete = models.PROTECT)
    address = models.CharField(max_length = 30, null = False)
    
# 경로당
class Senior_center(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)
    city = models.ForeignKey(City, on_delete = models.PROTECT)
    address = models.CharField(max_length = 50, null = False)
    tel = models.CharField(max_length = 25)

#교육 시설 (노인교실 / 평생학습포털)
class Edu_facility(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=10, primary_key = True)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)

#노인교실
class School(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    kind = models.ForeignKey(Edu_facility, on_delete = models.PROTECT)
    city = models.ForeignKey(City, on_delete = models.PROTECT)
    address = models.CharField(max_length = 50, null = False)
    tel = models.CharField(max_length = 15)

#노인교실 강좌 (노답)
'''
class School_lecture(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 30, primary_key = True)
'''

#강의 type
class Lecture(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 10, primary_key = True) #온/오프
    
#강의 genre
class Lecture_Genre(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 10, primary_key = True)

#평생교육시설
class Academy(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    kind = models.ForeignKey(Edu_facility, on_delete = models.PROTECT)
    city = models.ForeignKey(City, on_delete = models.PROTECT)
    tel = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    url = models.URLField()

#평생교육시설 강의들
class Academy_lecture(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 30, primary_key = True)
    type = models.ForeignKey(Lecture, on_delete = models.PROTECT)
    genre = models.ForeignKey(Lecture_Genre, on_delete = models.PROTECT)
    target = models.CharField(max_length = 300)
    level = models.CharField(max_length = 5)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank = True)
    url = models.URLField()
    

#두드림길 종류 5가지
class Course_type(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 10, primary_key=True)
    code = models.IntegerField(unique = True)

#두드림길    
class Course(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 50, primary_key = True)
    type = models.ForeignKey(Course_type, on_delete = models.PROTECT)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)
    city = ListCharField(base_field = models.CharField(max_length = 5), size=4, max_length = 4 * 6)
    level = models.CharField(max_length = 5)
    #city2 = models.ForeignKey(City, on_delete = models.PROTECT)
    #city3 = models.ForeignKey(City, on_delete = models.PROTECT)
    #city4 = models.ForeignKey(City, on_delete = models.PROTECT)
    length = models.CharField(max_length = 10)
    time = models.CharField(max_length = 10)
    desc = models.TextField()
    url = models.URLField()
    
#세부 코스
class Course_point(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    course = models.ForeignKey(Course, on_delete = models.PROTECT)
    desc = models.TextField()

class Culture_genre(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 10, primary_key = True)

#전시 관람    
class Exhibition(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 50, primary_key=True)
    available = models.BooleanField(default = False)
    location = models.CharField(max_length = 30)
    city = models.ForeignKey(City, on_delete = models.PROTECT)
    genre = models.ForeignKey(Culture_genre, on_delete = models.PROTECT)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)
    tel = models.CharField(max_length = 20)
    target = models.CharField(max_length = 50)
    url = models.URLField()
    image = models.URLField()
    starttime = models.CharField(max_length = 10)
    endtime = models.CharField(max_length = 10)

#서울시 행사
class Culture_Event(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 80, primary_key = True)
    genre = models.ForeignKey(Culture_genre, on_delete = models.PROTECT)
    kind = models.ForeignKey(Infrastructure, on_delete = models.PROTECT)
    startdate = models.DateField() 
    enddate = models.DateField() 
    location = models.CharField(max_length = 50)  #장소 위치 합쳐야댐
    target = models.CharField(max_length = 50)
    fare = models.CharField(max_length = 300)
    available = models.BooleanField(default = False)
    url = models.URLField(max_length = 300)
    image = models.URLField()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









