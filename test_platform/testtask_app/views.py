from django.shortcuts import render


def testtask_manage(request):
	"""
	任务管理
	"""
	return render (request, "task_list.html", {
		"type": "list"
	})



def add_task(request):
	"""
	创建任务
	"""
	return render (request, "task_add.html", {
		"type": "add"
	})


