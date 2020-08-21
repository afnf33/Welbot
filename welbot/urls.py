"""welbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'infrastructure', views.InfraViewSet)
router.register(r'wel_facility', views.WelFacilityViewSet)
router.register(r'senior_center', views.SeniorCenterViewSet)
router.register(r'edu_facility', views.EduViewSet)
router.register(r'school', views.SchoolViewSet)
router.register(r'lecture', views.LectureViewSet)
router.register(r'lecture_genre', views.LectureGenreViewSet)
router.register(r'academy', views.AcademyViewSet)
router.register(r'academy_lecture', views.AcademyLectureViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'course_type', views.CourseTypeViewSet)
router.register(r'course_point', views.CoursePointViewSet)
router.register(r'culture_genre', views.CultureGenreViewSet)
router.register(r'exhibition', views.ExhibitionViewSet)
router.register(r'culture_events', views.CultureEventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest/', include('rest.urls')),
]
