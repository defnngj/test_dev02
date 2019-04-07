"""test_platform URL Configuration

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
from django.urls import path
from personal.views import login_views
from personal.views import project_views
from personal.views import module_views
from js_demo import js_views


# 路由匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', login_views.say_hello),
    path('', login_views.index),
    path('index/', login_views.index),
    path('accounts/login/', login_views.index),
    path('logout/', login_views.logout),

    # project管理
    path('project/', project_views.project_manage),
    path('project/add_project/', project_views.add_project),
    path('project/edit_project/<int:pid>/', project_views.edit_project),

    path('module/', module_views.module_manage),

    path('js/', js_views.index),
    path('js_jisuan/', js_views.jisuan),


]
