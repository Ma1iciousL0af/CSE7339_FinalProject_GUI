from django.conf.urls import url

from . import views

app_name = 'gui'
urlpatterns = [
    url(r'^$', views.index, name='index'),
##    url(r'^$', views.upload_file, name='upload'),
##    url(r'^$', views.handle_uploaded_file, name='upload_handle')
]
