from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json


# Create your views here.
def testcase_manage(request):
    return render(request, "testcase.html", {"type": "debug"})


def testcase_debug(request):
    """
    测试用例的调试
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        print("url", url)
        print("method", method)
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

        result_text = None
        if method == "get":
            if header == "":
                r = requests.get(url, params=payload)
                result_text = r.text
            else:
                r = requests.get(url, params=payload, headers=header)
                result_text = r.text

        if method == "post":
            if type_ == "from":
                if header == "":
                    r = requests.post(url, data=payload)
                    result_text = r.text
                else:
                    r = requests.post(url, data=payload, headers=header)
                    result_text = r.text

            if type_ == "json":
                if header == "":
                    r = requests.post(url, json=payload)
                    result_text = r.text
                else:
                    r = requests.post(url, json=payload, headers=header)
                    result_text = r.text

        return JsonResponse({"result": result_text})
    else:
        return JsonResponse({"result": "请求方法错误"})


def testcase_assert(request):
    """
    测试用例的断言
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        print("断言类型", assert_type)

        if assert_type == "contains":
            assert_list = assert_text.split(">>")
            for assert_value in assert_list:
                if assert_value not in result_text:
                    return JsonResponse({"result": "断言失败"})
                else:
                    return JsonResponse({"result": "断言成功"})

        elif assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})

    else:
        return JsonResponse({"result": "请求方法错误"})




