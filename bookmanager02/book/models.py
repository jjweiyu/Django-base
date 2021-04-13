from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_time = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    # 1对多的关系模型中
    # 系统会自动为我们添加一个字段 关联模型类名小写__set
    #
    # peopleinfo_set = [PeopleInfo, PeopleInfo,...

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表名字
        verbose_name = '书籍管理'  # admin站点管理使用的（了解）

class PeopleInfo(models.Model):
    # 定义一个有序字典（枚举类型）
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    description = models.CharField(max_length=100, null=True)
    # 外键
    # 系统会自动为外键添加 _id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name