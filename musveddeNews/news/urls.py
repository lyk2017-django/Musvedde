from django.conf.urls import url
from news.views import *
from django.contrib.auth import views as view_auth

urlpatterns = [
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^category/(?P<slug>\w+)/$", CategoryView.as_view(), name="category_view"),
    url(r"^news/(?P<slug>[A-Za-z0-9\-]+)-(?P<pk>\d+)/$", NewsView.as_view(), name="news_view"),
    url(r"^tags/(?P<slug>\w+)$", TagsView.as_view(), name="tag_view"),
    url(r"^accounts/register/$", RegistrationView.as_view(), name="register"),
    url(r"^search/$", NewsSearchingView.as_view(), name="list-search"),
    url(r"^contact/$", ContactFormView.as_view(), name="contact"),
    url(r"^like/$", likeButton, name="like"),

]
