from django.contrib import admin
from rest.models import *


admin.site.register(City)
admin.site.register(Infrastructure)

#복지시설
admin.site.register(Wel_facility)
admin.site.register(Senior_center)

#교육시설
admin.site.register(Edu_facility)
admin.site.register(School)
admin.site.register(Lecture)
admin.site.register(Lecture_Genre)
admin.site.register(Academy)
admin.site.register(Academy_lecture)

#두드림길
admin.site.register(Course)
admin.site.register(Course_type)
admin.site.register(Course_point)

#문화행사
admin.site.register(Culture_genre)
admin.site.register(Exhibition)
admin.site.register(Culture_Event)

