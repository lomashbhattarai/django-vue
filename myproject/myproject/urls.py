"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from school.viewsets import UserViewSet,TeacherViewSet

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'teachers',TeacherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="application.html")),
    url(r'^', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
