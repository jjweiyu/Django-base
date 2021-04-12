from django.http import HttpResponse
from django.shortcuts import render


# 在视图函数中实现数据库的操作


def index(request):
    # return HttpResponse("index")
    # 模拟数据查询
    context = {
        "name": "用户登录"
    }
    return render(request, 'book/index.html', context=context)


from book.models import BookInfo
from book.models import PeopleInfo

##################添加数据####################

# 方式1
book = BookInfo(
    name="django",
    pub_time="2020-1-1",
    readcount=10
)
# 必须要调用对象的save方法才能将对象的数据保存到数据库
book.save()

# 方式2
# objects --> 相当于一个代理 实现增删改查
BookInfo.objects.create(
    name="HTML入门",
    pub_time="2008-3-13",
    readcount=133,
    commentcount=1200
)

##################修改数据####################

# 方式1
# select * from bookinfo where id=1
book = BookInfo.objects.get(id=1)
book.commentcount = 200
# 想要保存数据 需要调用 对象的save方法
book.save()

# 方式2
# filter 过滤
BookInfo.objects.filter(id=1).update(name='python', commentcount=666)

##################删除数据####################

# 方式1
book = BookInfo.objects.get(id=1)
# 删除分为2种，物理删除（删除这条记录的数据）  逻辑删除（修改标记位 例如 is_delete=False）
book.delete()

# 方式2
BookInfo.objects.get(id=2).delete()
BookInfo.objects.filter(id=3).delete()

##################查询数据####################

# get 查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print("查询结果不存在")

# all 查询多个结果
BookInfo.objects.all()
PeopleInfo.objects.all()

# count 查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

##################过滤查询####################
# 实现 SQL 中的 where 功能，包括
# filter 过滤出多个结果
# exclude 排除掉符合条件剩下的结果
# get 过滤单一结果
#
# 语法格式：
# 模型类名.objects.filter(属性名__运算符=值)        获取 n个结果  n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值)        获取 n个结果  n=0,1,2,...
# 模型类名.objects.get(属性名__运算符=值)        获取 1个结果  或者 异常

# 查询编号为 4的图书
book = BookInfo.objects.get(id=4)  # 简写形式  （属性名=值）
book = BookInfo.objects.get(id__exact=4)  # 完整形式
book = BookInfo.objects.get(pk=4)  # primary key 主键
book = BookInfo.objects.filter(id=4)

# 查询书名中包含'Java'的图书
BookInfo.objects.filter(name__contains='Java')

# 查询书名以'门'结尾的图书
BookInfo.objects.filter(name__endswith='门')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)  # 若没有，则返回空列表 不会报错

# 查询编号为 2 或 4 或 6的图书
BookInfo.objects.filter(id__in=(2, 4, 6))  # id__in=[2,4,6]

# 查询编号大于3的图书
# 大于 gt
# 小于 lt
# 大于等于 gte
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)

# 查询2008年发表的图书
BookInfo.objects.filter(pub_time__year=2008)

# 查询 2012年 1月 1日后发表的图书
BookInfo.objects.filter(pub_time__gt='2012-1-1')

#############################################################
from django.db.models import F

# 使用：2个属性的比较  还可以在F对象上使用算术运算
# 语法形式：以 filter为例     模型类名.objects.filter(属性名__运算符=F('第二个属性名'))
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

###############################################################

# 并且查询
# 查询阅读量小于30，并且编号大于3的图书
# 1>
BookInfo.objects.filter(readcount__lt=30).filter(id__gt=3)
# 2>
BookInfo.objects.filter(readcount__lt=30, id__gt=3)

# 或者查询
from django.db.models import Q

# 或者语法格式：   模型类名.objects.filter(Q(属性名__运算符=)|Q(属性名__运算符=)|...)
# 并且语法格式：   模型类名.objects.filter(Q(属性名__运算符=)&Q(属性名__运算符=)&...)
# not 非语法格式：   模型类名.objects.filter(~Q(属性名__运算符=))

# 查询阅读量大于30，或者编号小于3的图书
BookInfo.objects.filter(Q(readcount__gt=30) | Q(id__lt=3))

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

#####################聚合函数#################################
from django.db.models import Sum, Max, Min, Avg, Count

# 模型类名.objects.aggregate(Xxx('字段名'))
BookInfo.objects.aggregate(Sum('commentcount'))

#####################排序函数#################################
BookInfo.objects.all().order_by('readcount')  # 升序
BookInfo.objects.all().order_by('-readcount')  # 降序

#######################2个表的级联操作########################

# 查询书籍为 1的所有人物信息
book = BookInfo.objects.get(id=2)
book.peopleinfo_set.all()

# 查询人物为 1的书籍信息
person = PeopleInfo.objects.get(id=3)
var = person.book.name


#######################关联过滤查询########################

# 语法形式：  模型类名.objects.(关联模型类名小写__字段名__运算符=值)
# 查询 1的数据，条件为 n
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name__exact="郭靖")
BookInfo.objects.filter(peopleinfo__name="郭靖")

# 查询图书，要求图书中人物的描述信息包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')


# 查询书名为"python爬虫"的所有人物
PeopleInfo.objects.filter(book__name="python爬虫")
PeopleInfo.objects.filter(book__name__exact="python爬虫")

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)