from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.BusinessList.as_view(), name='all'),
    url(r'new/$', views.CreateBusiness.as_view(), name='create'),

]