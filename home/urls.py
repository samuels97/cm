from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    path('', views.index, name="home"),
    path('about_us/', views.aboutus, name="about_us"),
]
