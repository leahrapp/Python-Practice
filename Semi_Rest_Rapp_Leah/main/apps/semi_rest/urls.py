from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index, name='my_index'),
  url(r'^add_user$', views.add_user, name='add_user'),
  url(r'^add$', views.add, name='my_add'),
  url(r'^semi_rest/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
  url(r'^semi_rest/(?P<id>\d+)/save_edit$', views.save_edit, name='my_save_edit'),
  url(r'^semi_rest/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
  url(r'^semi_rest/(?P<id>\d+)/show$', views.show, name='my_show'),

  # This line has changed!
]