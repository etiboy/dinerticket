from django.conf.urls import url
from . import views

app_name = 'www'
urlpatterns = [
	url(r'^$',views.IndexView.as_view(),name='index'),
	url(r'^restaurant/(?P<pk>[0-9]+)/$',views.RestaurantView.as_view(),name='restaurant')
]