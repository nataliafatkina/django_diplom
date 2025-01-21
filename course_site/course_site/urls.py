from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from courses.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('registration/', register, name='registration'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('courses/', all_courses, name='all_courses'),
    path('courses/<str:username>/', user_courses, name='user_courses'),
    path('courses/course_<int:course_id>/', course_page, name='course_page'),
    path('courses/about_<int:course_id>/', about_course, name='about_course'),
    path('start_course_<int:course_id>/', start_course, name='start_course')
]
