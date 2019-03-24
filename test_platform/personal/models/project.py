from django.db import models

# Create your models here.
# MTV  ORM

# 在编程语言里面在夹杂了SQL语句
#
# python  -->  pymysql  -->  MySQL
# django --> ORM --> mymysql --> MySQL
# ORM  像操作对象一样的操作数据库


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=50, null=False)
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=1)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
