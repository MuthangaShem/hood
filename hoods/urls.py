from django.conf.urls import url
from . import views

app_name = 'hoods'
urlpatterns = [
    url(r'^$', views.ListHoods.as_view(), name='all'),
    url(r'^new/$', views.CreateHood.as_view(), name='create'),
    url(r'businesses/in/(?P<slug>[-\w]+)/$', views.SingleNeighbourhood.as_view(), name='single'),

]