from django.conf.urls import url
from dinosaurOrigin import views


urlpatterns = [
    url(r'^$', views.dinosaurOrigin, name='dinosaurOrigin'),
]