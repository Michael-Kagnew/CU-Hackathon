from django.conf.urls import url, include

from contracts.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^create_contract$', create_contract, name='create_contract'),

]