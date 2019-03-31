from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from personal.models.project import Project


# MTV  view
def say_hello(request):
    input_name = request.GET.get("name", "")
    if input_name == "":
        return HttpResponse("请求输入?name=name")
    return render(request, "index.html", {"name": input_name})


# 登录的首页
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {
                "error": "用户名或密码为空"})

        user = auth.authenticate(username=username, password=password)
        print("user-->", user)
        if user is None:
            return render(request, "index.html", {
                "error": "用户名或密码错误"})
        else:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect("/project/")

# 处理用户的退出
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")






"""

web开发，一般的web框架：
mvc 

Model（模型）表示应用程序核心（比如数据库记录列表）。
View（视图）显示数据（数据库记录）。
Controller（控制器）处理输入（写入数据库记录）

mtv
Model -- model
templeate 模板 -- view
view --- Controller
"""

#客户端（浏览器） --->request     服务器（django）
#客户端（浏览器） Response<---    服务器（django）

# django 引用 bootstrap
# 1、使用 cdn
# 2、把资源文件放到本地 static/
# 3、用django-bootstrap 插件（扩展）












