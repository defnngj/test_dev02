from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User


class MyLoginTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = Chrome()
        cls.selenium.implicitly_wait(10)

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_null(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/index/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        error = self.selenium.find_element_by_id("error").text
        self.assertEquals(error, "username or password null")

    def test_login_username_null(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/index/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('123456')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        error = self.selenium.find_element_by_id("error").text
        self.assertEquals(error, "username or password null")

    def test_login_password_null(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/index/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        error = self.selenium.find_element_by_id("error").text
        self.assertEquals(error, "username or password null")

    def test_login_error(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/index/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('error')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('error')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        error = self.selenium.find_element_by_id("error").text
        self.assertEquals(error, "username or password error")
    
    def test_login_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/index/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin123456')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        title = self.selenium.find_element_by_id("title").text
        self.assertEquals(title, "接口测试平台")
