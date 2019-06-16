import json
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from project_app.models import Project
from module_app.models import Module
from testcase_app.models import TestCase
from testtask_app.models import TestTask



def testtask_manage(request):
	"""
	任务管理
	"""
	task_list = TestTask.objects.all()

	return render (request, "task_list.html", {
		"type": "list",
		"tasks": task_list
	})


def add_task(request):
	"""
	返回创建任务页面
	"""
	return render (request, "task_add.html", {
		"type": "add"
	})


def edit_task(request, tid):
	"""
	返回编辑任务页面
	"""
	return render(request, "task_edit.html", {
		"type": "edit"
	})


def delete_task(request, tid):
	"""
	删除任务
	"""

	task = TestTask.objects.get(id=tid)
	task.delete()

	return HttpResponseRedirect("/testtask/")


def save_task(request):
	"""
	创建/编辑任务
	"""
	if request.method == "POST":
		task_id = request.POST.get("task_id", "")
		name = request.POST.get("name", "")
		desc = request.POST.get("desc", "")
		cases = request.POST.get("cases", "")
		print("name", name, desc)
		print("用例", type(cases), cases)
		
		if name == "" or cases == "":
			return JsonResponse({"status": 10102, "message": "Parameter is null"})
		
		print("任务的id--->", task_id)
		if task_id == "0":
			print("创建")
			TestTask.objects.create(name=name, describe=desc, cases=cases)
		else:
			print("编辑")
			task = TestTask.objects.get(id=task_id)
			task.name = name 
			task.describe = desc
			task.cases = cases
			task.save()

		return JsonResponse({"status": 10200, "message": "success"})
	else:
		return JsonResponse({"status": 10101, "message": "请求方法错误"})


def get_case_tree(request):
	"""
	获得用例树形结构
	"""
	if request.method == "GET":
		projects = Project.objects.all()
		data_list = []
		for project in projects:
			project_dict = {
				"name": project.name,
				"isParent": True
			}
			
			modules = Module.objects.filter(project_id=project.id)
			module_list = []
			for module in modules:
				module_dict = {
					"name": module.name,
					"isParent": True
				}
				
				cases = TestCase.objects.filter(module_id=module.id)
				case_list = []
				for case in cases:
					case_dict = {
						"name": case.name,
						"isParent": False,
						"id": case.id,
					}
					case_list.append(case_dict)
				
				module_dict["children"] = case_list
				module_list.append(module_dict)
			
			project_dict["children"] = module_list
			data_list.append(project_dict)
		
		return JsonResponse({"status": 10200, "message": "success", "data": data_list})
	
	if request.method == "POST":
		tid = request.POST.get("tid", "")
		print("任务的id", tid)
		if tid == "":
			return JsonResponse({"status": 10200, "message": "任务id不能为空"})
		
		task = TestTask.objects.get(id=tid)
		casesList = json.loads(task.cases)
		task_data = {
			"name": task.name,
			"desc": task.describe
		}
		
		projects = Project.objects.all()
		data_list = []
		for project in projects:
			project_dict = {
				"name": project.name,
				"isParent": True
			}

			modules = Module.objects.filter(project_id=project.id)
			module_list = []
			for module in modules:
				module_dict = {
					"name": module.name,
					"isParent": True
				}

				cases = TestCase.objects.filter(module_id=module.id)
				case_list = []
				for case in cases:
					if case.id in casesList:
						case_dict = {
							"name": case.name,
							"isParent": False,
							"id": case.id,
							"checked": True,
						}
					else:
						case_dict = {
							"name": case.name,
							"isParent": False,
							"id": case.id,
							"checked": False,
						}
					case_list.append(case_dict)

				module_dict["children"] = case_list
				module_list.append(module_dict)

			project_dict["children"] = module_list
			data_list.append(project_dict)
		task_data["cases"] = data_list
		return JsonResponse({"status": 10200, "message": "success", "data": task_data})


def run_task(request):
	""" 运行任务 """
	if request.method == "POST":
		tid = request.POST.get("task_id", "")
		if tid == "":
			return JsonResponse({"status": 10200, "message": "task id is null"})
		task = TestTask.objects.get(id=tid)
		print(task.cases)
		print("--->", list(task.cases))
		case_list = json.loads(task.cases)
		print("===>", case_list)
		test_data = {}
		for cid in case_list:
			print("wtf", cid)
			case = TestCase.objects.get(id=cid)
			if case.method == 1:
				method = "get"
			elif case.method == 2:
				method = "post"
			else:
				method = "null"
			
			if case.parameter_type == 1:
				parameter_type = "from"
			else:
				parameter_type = "json"

			if case.assert_type == 1:
				assert_type = "contains"
			else:
				assert_type = "mathches"
			
			test_data[case.id] = {
				"url": case.url,
				"method": method,
				"header": case.header,
				"parameter_type": parameter_type,
				"parameter_body": case.parameter_body,
				"assert_type": assert_type,
				"assert_text": case.assert_text,
			}
		print("任务下面的用例", json.dumps(test_data))
		case_data = json.dumps(test_data)

		from test_platform import settings
		
		EXTEND_DIR = settings.BASE_DIR + "\\testtask_app\\extend\\"
		print("项目的基本路径", EXTEND_DIR)
		with(open(EXTEND_DIR + "test_data_list.json", "w")) as f:
			f.write(case_data)
		run_cmd = "pytest -vs " + EXTEND_DIR+ "run_task.py --junitxml="+EXTEND_DIR+"log.xml"
		print("运行的命令", run_cmd)
		os.system(run_cmd)
		return JsonResponse({"status": 10200, "message": "任务执行完成"})
	else:
		return JsonResponse({"status": 10200, "message": "success", "data": task_data})

