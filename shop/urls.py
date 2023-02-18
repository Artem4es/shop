"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView

from main_page import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('yandex_551046113a1adf80.html', views.yandex_webmaster),
    path('google91b4364c93644c83.html', views.google),
    path('favicon.ico',RedirectView.as_view(url='/static/assets/turbo.png')),
    path('admin/', admin.site.urls),

]

