from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'rest'

urlpatterns = [
    path('test/', views.index, name='test'),
    path('city_init/', views.city_init, name='city_init'),
    path('infra_init/', views.infra_init, name='infra_init'),
    path('edu_init/', views.edu_init, name='edu_init'),
    path('course_type/', views.course_type, name='course_type_init'),
    path('senior_center/', views.senior_center_init, name='senior_center_init'),
    path('wel_facility/', views.wel_facility_init, name='wel_facility_init'),
    path('school/', views.school_init, name='school_init'),
    path('lecture/', views.lecture_init, name='lecture_init'),
    path('academy/', views.academy_init, name='academy_init'),
    path('course/', views.course_init, name='course_init'),
    path('culture_genre_init/', views.culture_genre_init, name='culture_genre_init'),
    path('exhibition_init/', views.exhibit_init, name='exhibition_init'),
    path('culture_event_init/', views.culture_event_init, name='culture_event_init'),
    path('academy_lecture/', views.academy_lect_init, name='academy_lecture_init'),
    path('api/', views.webhook, name='api'),
    ]