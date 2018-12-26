"""myforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from app01 import views
from app02 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.user),
    path('add_user/', views.add_user),
    re_path('edit_user-(\d+)/', views.edit_user),
    path('test/', v2.test),
    path('xq/', v2.xq),
    path('ajax/', v2.ajax),
]
