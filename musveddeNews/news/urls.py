from django.conf.urls import url
from news.views import *


urlpatterns =[
    url(r"^$",HomeView.as_view(),name="home"),
    url(r"^category/(?P<slug>[A-Za-z0-9\-]+)$",CategoryView.as_view(), name="category_view"),
    url(r"^news/(?P<id>\d+)-(?P<slug>[A-Za-z0-9\-]+)$",NewsView.as_view(), name="news_view" ),
]

