from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from web_client import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='homepage'),
    url(r'^ajax/navbar/$', views.Navbar.as_view(), name='load_navbar'),
    url(r'^ajax/main_content/$', views.MainContent.as_view(), name='load_main_content'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^ajax/search_form/$', views.Search.as_view(), name='search'),
    # url(r'^ajax/search_results/$', views.Search.as_view(), name='search'),
]