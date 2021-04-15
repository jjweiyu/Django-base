from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

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

    ###################请求头#################
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

"""

第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?username=jing&password=123
服务器接收到请求后，获取username，然后服务器设置cookie信息，cookie信息包括 username
浏览器接收到服务器的响应后，应该把cookie保存起来

第二次及其之后的请求，我们访问http://127.0.0.1:8000 都会携带cookie信息。服务器可以读取cookie信息来判断用户身份
"""


def set_cookie(request):
    # 1. 获取查询字符串中的数据
    username = request.GET.get("username")
    password = request.GET.get("password")
    # 2. 服务器设置cookie信息 通过响应对象的 set_cookie方法
    response = HttpResponse("set_cookie")
    # 第一个参数 key 设置 cookie的名称
    # 第二个参数 value 设置该 cookie的内容
    # 第三个参数 max_age 设置cookie 的结束时间  是一个秒数
    response.set_cookie('name', username, max_age=3600)
    response.set_cookie('password', password)

    # 删除 cookie
    response.delete_cookie("password")
    return response


def get_cookie(request):
    # 专门通过请求对象 request.COOKIES 方法获取请求头中的 cookie信息
    print(request.COOKIES)  # 是字典数据
    name = request.COOKIES.get("name")
    return HttpResponse(name)


#########################session##########################
# session 是保存在服务器端   --- 数据相对安全
# session 需要依赖于 cookie    --- cookie被禁用，session就使用不了

"""

第一次请求 http://127.0.0.1:8000/set_session/?username=weiyu  我们在服务器端设置session信息
服务器会生成一个seesionid的cookie信息
浏览器接受到这个信息之后，会把cookie数据保存起来

第二次及其之后的请求 都会携带这个sessionid，服务器会验证这个sessionid，验证没有问题会读取相关数据 实现业务逻辑

"""


def set_session(request):
    # 1. 模拟 获取用户信息
    username = request.GET.get("username")

    # 2. 设置session信息  request.session["key"] = value
    # 设置的 键值对 是保存到 django_session表中的 session_data中的
    # 假如 我们通过模型查询 查询到了用户信息
    user_id = 1
    request.session["user_id"] = user_id
    request.session["username"] = username

    # clear 删除 session里的数据，但是 key有保留
    request.session.clear()
    # flush 是删除所有的数据，包括 key
    request.session.flush()

    # 设置session的有效时间
    request.session.set_expiry(None)

    return HttpResponse("set_session")


def get_session(request):
    user_id = request.session.get("user_id")
    username = request.session.get("username")
    # 格式化字符串的函数 str.format()
    # 类似于格式化输出 '%s' %(user_id, username)
    content = '{},{}'.format(user_id, username)
    return HttpResponse(content)


######################类视图#############################

def login(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse("GET 逻辑")
    else:
        return HttpResponse("POST 逻辑")


"""
类视图的定义

class 类视图名字(View):
    def get(self,request):
        return HttpResponse('xxx')
    def post(self,request):
        return HttpResponse('xxx')

1. 继承自View
2. 类视图的方法 是采用 http 请求方法 小写来区分不同的请求方式
"""
from django.views import View


class LoginView(View):
    def get(self, request):
        return HttpResponse("get get")

    def post(self, request):
        return HttpResponse("post post")
