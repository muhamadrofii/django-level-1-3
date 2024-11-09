"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django1 import views as django1_views
from django3 import views as django3_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('subscribe/', django3_views.subscribe_view, name='subscribe'),  # View dari django3
    path('customers/', django3_views.customer_list, name='customer_list'), # View dari django3
    path('', django1_views.index, name='index'),  # View dari django1
]

