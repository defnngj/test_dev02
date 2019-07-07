from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


## django test 不会读取本地数据库里面的数据

class SayHelloTest(TestCase):
	
	def test_say_hello_name_none(self):
		c = Client()
		response = c.get('/hello/')
		statust = response.status_code
		content = str(response.content)
		print(statust)
		print(content)
		self.assertEquals(statust, 200)
		self.assertIn("please input", content)

	def test_say_hello_name_tom(self):
		c = Client()
		response = c.get('/hello/?name=tom')
		statust = response.status_code
		content = str(response.content)
		print(statust)
		print(content)
		self.assertEquals(statust, 200)
		self.assertIn("hello", content)


class IndexTest(TestCase):

	def test_get_index_page(self):
		c = Client()
		response = c.get('/index/')
		statust = response.status_code
		content = str(response.content)
		# print(statust)
		# print(content)
		self.assertEquals(statust, 200)
		# self.assertIn("interface test platform", content)
		self.assertTemplateUsed(response, 'index.html')


class LoginTest(TestCase):

	def setUp(self):
		 User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

	def test_login_null(self):
		c = Client()
		login_user = {'username': '', 'password': ''}
		response = c.post('/index/', login_user)
		statust = response.status_code
		content = str(response.content)
		print(statust)
		print(content)
		self.assertEquals(statust, 200)
		self.assertTemplateUsed(response, 'index.html')
		self.assertIn("username or password null", content)

	def test_login_error(self):
		c = Client()
		login_user = {'username': 'error', 'password': 'error'}
		response = c.post('/index/', login_user)
		statust = response.status_code
		content = str(response.content)
		print(statust)
		print(content)
		self.assertEquals(statust, 200)
		self.assertTemplateUsed(response, 'index.html')
		self.assertIn("username or password error", content)

	def test_login_success(self):
		c = Client()
		login_user = {'username': 'admin', 'password': 'admin123456'}
		response = c.post('/index/', login_user)
		statust = response.status_code
		print(statust)
		self.assertEquals(statust, 302)
