from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [

    url(r'^$', views.process_request, name='process_request'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^book/$',views.query_books, name='query_books'),
    url(r'^user/$',views.query_users, name='query_users'),
    url(r'^user/new/$',views.add_user,name='add_user'),
    url(r'^author/$',views.query_authors, name='query_authors')
]
