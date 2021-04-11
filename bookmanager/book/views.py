from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("index")
    # 模拟数据查询
    context = {
        "name": "用户登录"
    }
    return render(request,'book/index.html', context=context)
