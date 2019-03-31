from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def module_manage(request):
    """
    模块管理
    """
    return render(request, "module.html")
