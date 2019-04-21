from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.
def testcase_manage(request):
    return render(request, "testcase.html", {"type": "debug"})


def debug(request):
    if request.method == "POST":
        url = request.POST.get("url", "")
        moethd = request.POST.get("moethd", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        print("url", url)
        print("moethd", moethd)
        print("header", header)
        print("type_", type_)
        print("parameter", parameter)

        json_header = header.replace("\'", "\"")
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        json_par = parameter.replace("\'", "\"")
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        if moethd == "get":
            if header == "":
                r = requests.get(url, params=payload)
                print("结果", r.json())
            else:
                r = requests.get(url, params=payload, headers=header)
                print("结果", r.json())

        if moethd == "post":
            if type_ == "from":
                if header == "":
                    r = requests.post(url, data=payload)
                    print(r.text)
                else:
                    r = requests.post(url, data=payload, headers=header)
                    print(r.text)

            if type_ == "json":
                if header == "":
                    r = requests.post(url, json=payload)
                    print(r.text)
                else:
                    r = requests.post(url, json=payload, headers=header)
                    print(r.text)

        return JsonResponse({"result": r.text})
    else:
        return JsonResponse({"result": "请求方法错误"})


