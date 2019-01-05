"""myproject URL Configuration

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
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.urls import path

from boards import views
from accounts import views as acc_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<int:question_id>',views.question_detail,name='question_detail'),
    path('new',views.add_question,name='add_question'),
    path('signup',acc_views.signup,name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('search', views.search.as_view(), name='search'),
    path('<int:question_id1>/newanswer', views.add_answer, name='new_answer'),



]
