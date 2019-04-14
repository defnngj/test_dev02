from django.db import models


# Create your models here.
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
