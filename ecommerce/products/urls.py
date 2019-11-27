from django.conf.urls import url
from django.views.generic import ListView,DetailView
from products.views import ProductListView,DetailListView

urlpatterns = [
    url(r'^$',ProductListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',DetailListView.as_view(),name='detail'), 
]