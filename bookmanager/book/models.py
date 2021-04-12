from django.db import models

# Create your models here.
"""
1. 模型类需要维承自models.Model
2．定义属性
    id系统默认会生咸
    属性名=models.类型（选项)
    2.1 属性名对应就是字段名
            不要使用python,MySQL关键字
            不要使用连续的下划线(__)
    2.2 类型 MySQL的类型
    2.3 选项 是否有默认值,是否唯一,是否为null
            charField 必须设置 max_length 
            verbose_name主要是admin站点使用
3. 修改表的名称
    默认表的名称是： 子应用名_类名 都是小写
    修改表的名称： 在类中定义一个类：
                            class Meta：
                                db_table = '新名字'
create table qq_user(
    id int ,
    name varchar(10) not null default ''
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_time = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改表名字
        verbose_name = '书籍管理'  # admin站点管理使用的（了解）


class PeopleInfo(models.Model):
    # 定义一个有序字典（枚举类型）
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0)
    description = models.CharField(max_length=100, null=True)
    # 外键
    # 系统会自动为外键添加 _id
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

