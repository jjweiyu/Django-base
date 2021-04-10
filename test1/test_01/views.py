from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是Python函数
视图函数有2个要求：
    1. 视图函数的第一个参数就是接受请求。这个请求其实就是 HttpRequest 的类对象
    2. 必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入 http://127.0.0.1:8000/index
# 来访问视图函数

def index(request):
    # return HttpResponse("ok")

    # render 渲染模板
    # request, template_name, context=None
    # request --> 请求
    # template_name --> 模板名字
    # context=None
    # 准备上下文：定义在字典中（测试数据）
    context={
        "name": "马上双十一，点击有惊喜"
    }
    # 将上下文交给模板中进行处理，处理后视图响应给客户端
    return render(request, 'test_01/index.html', context=context)
