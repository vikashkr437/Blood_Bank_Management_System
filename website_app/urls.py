from django.conf.urls import url
from website_app import views

# TEMPLATE TAGGING
app_name = 'website'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^registerdonor/', views.registerdonor, name='registerdonor'),
    url(r'^registerhospital/', views.registerhospital, name='registerhospital'),
    url(r'^output/',views.output, name='output'),
    url(r'^availability/',views.availability, name='availability'),
    url(r'^order/',views.orderfun, name='order'),

]

