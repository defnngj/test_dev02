from django.test import TestCase
from project_app.models import Project
from django.test import Client
from django.contrib.auth.models import User


class ProjectTest(TestCase):

	def setUp(self):
		Project.objects.create(id=1, name="AA项目", 
                         		describe="测试专用",
						 		status=1)

	# 测试查询
	def test_query(self):
		project = Project.objects.get(id=1)
		name = project.name
		desc = project.describe
		self.assertEquals(name, "AA项目")
		self.assertEquals(desc, "测试专用")

	# 测试增加
	def test_add(self):
		Project.objects.create(id=2, name="BB项目",
                         describe="开发专用",
                         status=1)
		project = Project.objects.get(id=2)
		name = project.name
		desc = project.describe
		self.assertEquals(name, "BB项目")
		self.assertEquals(desc, "开发专用")

	# 测试更新
	def test_update(self):
		project = Project.objects.get(id=1)
		project.name = "AA任务"
		project.describe = "任务的描述"
		project.save()
		project = Project.objects.get(id=1)
		self.assertEquals(project.name, "AA任务")
		self.assertEquals(project.describe, "任务的描述")

	# 测试删除
	def test_delete(self):
		project = Project.objects.all()
		print("删除前", len(project))

		project = Project.objects.get(id=1)
		project.delete()
		
		project = Project.objects.all()
		print("删除后", len(project))

		self.assertEquals(len(project), 0)


class ProjectManageTest(TestCase):

	def setUp(self):
		Project.objects.create(id=1, name="AA Porject", describe="describe",
                         						 		status=1)
		User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
		login_user = {'username': 'admin', 'password': 'admin123456'}
		self.client.post('/index/', login_user)
	
	def test_project_manage_page(self):
		response = self.client.get('/project/')
		statust = response.status_code
		content = str(response.content)
		print(statust)
		print(content)
		self.assertEquals(statust, 200)
		self.assertIn("AA Porject", content)
		self.assertTemplateUsed(response, 'project.html')
