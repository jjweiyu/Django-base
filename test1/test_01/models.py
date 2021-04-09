from django.db import models

# Create your models here.
"""
    1.我们的模型类 需要继承自 models.Model
    2.每一个模型类就相当于数据库中的一个数据表
    3.系统会自动为我们添加一个主键--id
    4.字段

        字段名=model.类型（选项）
        字段名就是数据表的字段名
        字段名不要使用 Python 和 mysql 的关键字
        char(M)
        varchar(M)
        M就是选项
"""


class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=20)


# 人物类 先复制过来，后期讲原理
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
