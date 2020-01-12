from django.conf.urls import url, include

from profiles.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),

    url(r'^edit_profile$', edit_profile, name='edit_profile'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^view_profile$', view_profile, name='view_profile'),

]