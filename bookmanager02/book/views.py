from django.http import HttpResponse
from django.shortcuts import render

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


def shop(request, city_id, shop_id):
    print(city_id, shop_id)

    query_params = request.GET
    print(query_params)
    # 输出结果为：查询字典 <QueryDict: {'order': ['readcount']}>
    # 获取键值： order = query_params.get('order')
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    # <QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']}>
    # 当含有多个值的时候需要用 getlist 来获取键值
    return HttpResponse("小饭店")


"""
查询字符串

http://ip:port/path/../path/?key1=value1&key2=value2&...

url 以 ? 为分隔 分为2部分
? 前边的是 请求路径
? 后边的是 查询字符串 类似于字典 key=value 多个数据采用 & 拼接
"""
