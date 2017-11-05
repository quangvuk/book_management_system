"""book_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from ezmanagement import views as ez_views
from django.contrib.auth.views import login

urlpatterns = [
                  # url(r'^login/',ez_views.login_user),
                  # url(r'^login/',login, {'template_name':'../ezmanagement/templates/login.html'}),
                  # url(r'^logout/', ez_views.logout_user),
                  # url(r'^home/',ez_views.home),
                  # url(r'^admin/', admin.site.urls),
                  #url(r'^$')
                  url(r'^api/', include('api.urls', namespace='api')),
                  url(r'^ezmanagement/', include('ezmanagement.urls', namespace='ezmanagement')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    url(r'^accounts/', RedirectView.as_view(url='ezmanagement/')),
]

# if settings.DEBUG is True:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
