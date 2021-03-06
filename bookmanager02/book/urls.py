from django.urls import path, converters

from book.views import create_book, shop, register, json, response, test, red, set_cookie, get_cookie, set_session, \
    get_session, LoginView, OrderView
from django.urls.converters import register_converter


# 1. 定义转换器
class MobileConverter:
    # 验证数据的关键是： 正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数
    def to_python(self, value):
        return int(value)  # 具体看需求返回，也可以 return str(value)

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
    path('json/', json),
    path('res/', response),
    path('test/', test),
    path('redirect/', red),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    ########类视图###########33
    path('163login/', LoginView.as_view()),
    path('order/', OrderView.as_view())
]
"""
class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""
