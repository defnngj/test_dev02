from django.urls import path
from testtask_app import views


urlpatterns = [
    # 任务管理
    path('', views.testtask_manage),
	path('add_task/', views.add_task),
	path('edit_task/<int:tid>/', views.edit_task),
	path('delete_task/<int:tid>/', views.delete_task),
   	path('save_task/', views.save_task),

    path('get_case_tree/', views.get_case_tree)
]
