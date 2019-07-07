from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# MTV  view
def say_hello(request):
    input_name = request.GET.get("name", "")
    if input_name == "":
        return HttpResponse("please input ? name")
    return HttpResponse("hello," + input_name)


# 登录的首页
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "username or password null"})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "username or password error"})
        else:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect("/project/")


# 处理用户的退出
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")



