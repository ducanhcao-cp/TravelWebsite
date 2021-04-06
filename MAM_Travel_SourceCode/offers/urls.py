from django.urls import path
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
app_name = 'offers'
urlpatterns = [
    path('', views.offers, name='offers'),
    path('getDeal/', views.getDeal, name='getDeal'),
    path('<int:id>/', views.offersDetail, name='offersDetail'), 
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)