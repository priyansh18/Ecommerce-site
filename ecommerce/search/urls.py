from django.conf.urls import url
from django.views.generic import ListView
from search.views import SearchListView

urlpatterns = [
    url(r'^$',SearchListView.as_view(), name='searching')
]