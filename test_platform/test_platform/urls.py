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
from django.urls import path, include
from user_app import views
from js_demo import js_views


# 路由匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户应用
    path('hello/', views.say_hello),
    path('', views.index),
    path('index/', views.index),
    path('accounts/login/', views.index),
    path('logout/', views.logout),

    # 项目管理
    path('project/', include('project_app.urls')),
    # 模块管理
    path('module/', include('module_app.urls')),
    # 用例管理
    path('testcase/', include('testcase_app.urls')),

    # js例子--删除
    path('js/', js_views.index),
    path('js_jisuan/', js_views.jisuan),

    # 重构  在功能不变的基础上修改代码的结构

]
