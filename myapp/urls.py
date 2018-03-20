from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^post1/(\d+)$',views.post1),

]
