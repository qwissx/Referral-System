"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', views.AccountList.as_view()),
    path('account/<str:pk>/', views.AccountDetails.as_view()),
    path('account/auth/send-code/', views.send_code),
    path('account/auth/verify-code/', views.verify_code),
    path('form/account/auth/send-code', views.send_code_form),
    path('form/account/auth/verify-code', views.verify_code_form),
]
