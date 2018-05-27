from django.conf.urls import url
from . import views

app_name = 'neighbourhoods'
urlpatterns = [
    url(r'^$', views.ListHoods.as_view(), name='all'),
]