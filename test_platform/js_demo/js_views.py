from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, "js_demo.html")


# 测试的接口
def jisuan(request):
    if request.method == "POST":
        n1 = request.POST.get("num1", "")
        n2 = request.POST.get("num2", "")
        if n1 == "" or n2 == "":
            return JsonResponse({"status_code": 10011,
                                 "message": "参数不能为空"})
        try:
            n1 = int(n1)
            n2 = int(n2)
        except ValueError:
            return JsonResponse({"status_code": 10012,
                                 "message": "参数类型错误"})

        return JsonResponse({"status_code": 10200,
                             "message": "成功",
                             "data": n1+n2})
    else:
        return JsonResponse({"status_code": 10010,
                             "message": "请求方法错误"})
