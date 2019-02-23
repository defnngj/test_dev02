from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# MTV  view
def say_hello(request):
    name = request.GET.get("name", "")
    talk = []
    for n in range(3):
        talk.append("hello," + name + "<br>")
    return HttpResponse(talk)



#客户端（浏览器） --->request     服务器（django）
#客户端（浏览器） Response<---    服务器（django）