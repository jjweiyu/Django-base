from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from book.models import BookInfo


def create_book(request):
    book = BookInfo.objects.create(
        name="高数36讲",
        pub_time="2021-3-4",
        readcount=200,
        commentcount=500
    )
    return HttpResponse("create")


def shop(request, city_id, mobile):
    # 通过正则表达式进行URL中的参数判断
    # import re
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse("没有此商品")

    print(city_id, mobile)

    query_params = request.GET
    print(query_params)
    # 输出结果为：查询字典 <QueryDict: {'order': ['readcount']}>
    # 获取键值： order = query_params.get('order')
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    # <QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>
    # 当含有多个值的时候需要用 getlist 来获取键值
    return HttpResponse("小饭店")

def register(request):
    # 获取 form表单数据
    data = request.POST
    print(data)
    # <QueryDict: {'username': ['jing'], 'password': ['123']}>
    return HttpResponse("ok")

def json(request):
    # json数据不能通过 request.POST获取,需要通过 request.body接收
    body = request.body
    # print(body)
    # b'{\r\n    "name":"jing",\r\n    "age":18\r\n}'
    body_str = body.decode()
    print(body_str)
    # 字符串类型的数据
    # {
    #     "name":"jing",
    #     "age":18
    # }
    # JSON形式的字符串可以转换为 python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)

    ###########请求头##########
    # 获取请求头信息   字典类型
    # print(request.META)
    print(request.META.get('SERVER_PORT'))
    return HttpResponse("json")


def response(request):
    info = {
        "name": '魏哲宇',
        "address": '华北水利水电大学'
    }
    girl = [
        {
            "name": '魏哲宇',
            "address": '华北水利水电大学'
        },
        {
            "name": '王佳伟',
            "address": '华北水电水利大学'
        }
    ]
    # data参数 返回的响应数据 一般是字典类型
    """
    safe = True 是表示我们的 data 是字典数据
    JsonResponse 可以把字典转换为  json
    
    现在给了一个非字典数据，safe = False 意思是出了问题我们自己负责
    """
    # response = JsonResponse(data=girl)
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    # 提示我们传入一个非字典数据的数据，就要修改 JsonResponse 中的 safe 参数值为 False
    response = JsonResponse(data=girl, safe=False)
    return response


    # return HttpResponse('res', status=200)
    # 状态码
    # 1xx
    # 2xx
    # 3xx
    # 4xx  请求有问题
        # 404 找不到页面  路由有问题
        # 403 禁止访问   权限问题
    # 5xx
    # HTTP status code must be an integer from 100 to 599.


def test(request):
    str = "weizheyu is idiolt"
    response = JsonResponse(data=str, safe=False)
    return response


def red(resquest):
    return redirect("http://www.baidu.com")
"""
查询字符串

http://ip:port/path/../path/?key1=value1&key2=value2&...

url 以 ? 为分隔 分为2部分
? 前边的是 请求路径
? 后边的是 查询字符串 类似于字典 key=value 多个数据采用 & 拼接
"""
