from django.urls import path
from . import views 
#from django.contrib.auth import views as auth_views 
app_name = 'home'
urlpatterns = [
    path('', views.index, name='home'),
    path('dang-ki/', views.register, name='register')
    #path('login/', auth_views.login, name='login')
]