from django.conf.urls import url, include

from login.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),

    url(r'^signin$', signin, name='signin'),
    url(r'^signup$', signup, name='signup'),
    url(r'^signout$', signout, name='signout'),
]