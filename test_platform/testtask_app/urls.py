from django.urls import path
from testtask_app import views


urlpatterns = [
    # 任务管理
    path('', views.testtask_manage),
	path('add_task/', views.add_task),
]
