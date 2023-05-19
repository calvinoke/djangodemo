
from django.urls import path
from app import views

urlpatterns = [
    path('', views.hello),
    path('index/', views.index),
    path('show/',  views.show),
    path('employee', views.emp),
    path('indexs', views.indexs),
    path('info',views.methodinfo),
    path('ssession',views.setsession),
    path('gsession',views.getsession),
    path('scookie',views.setcookie),
    path('gcookie',views.getcookie),
    path('csv',views.getfiles),
    path('pdf',views.getpdf),
]