from django.urls import path, converters

from book.views import create_book, shop, register, json
from django.urls.converters import register_converter


# 1. 定义转换器
class MobileConverter:
    # 验证数据的关键是： 正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数
    def to_python(self, value):
        return int(value)   # 具体看需求返回，也可以 return str(value)

    # def to_url(self, value):
    #     return str(value)


# 2. 先注册转换器，才能在第三步中使用
# conventer 转换器类
# type_name 转换器名字
register_converter(MobileConverter, 'phone')
urlpatterns = [
    path('create/', create_book),
    #
    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则的验证
    # 3. 使用转换器
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json)
]
"""
class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""
