"""HospitalAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
admin.site.site_header = "DK HospitalAPI Admin"
admin.site.site_title = "DK HospitalAPI Admin Panel"
admin.site.index_title = "Welcome to DK HospitalAPI Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
