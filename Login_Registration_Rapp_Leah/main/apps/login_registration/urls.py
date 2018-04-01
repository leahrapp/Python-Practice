from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index, name='my_index'),
  url(r'^add_user$', views.add_user, name='add_user'),
  url(r'^success$', views.success, name='success'),
  url(r'^login$', views.login, name='login'),

  # This line has changed!
]