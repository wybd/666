"""python URL Configuration

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
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',views.index),
    # path('giao',views.giao),
    # re_path("^$",views.giao),
    # re_path("demo/(\d)/",views.demo)
    # re_path('zhengze/(\d{4})/(\w+)/',views.zhengze),
    # re_path('demo02/(?P<year>\d{4})/(?P<where>\w*)',views.demo02),
    re_path('datys/(?P<year>\d{4})/(?P<mouth>\d{2})/(?P<day>\d{2})',views.datys)

]
