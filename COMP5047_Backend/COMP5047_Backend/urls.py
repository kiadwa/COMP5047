"""
URL configuration for COMP5047_Backend project.

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

import COMP5047_Backend.API.FileHandler

urlpatterns = [
    path('tts', COMP5047_Backend.API.FileHandler.tts),
    path('tts/result', COMP5047_Backend.API.FileHandler.get_tts_result),
    path('tts/premade/<str:text>', COMP5047_Backend.API.FileHandler.get_premade_result)
]
