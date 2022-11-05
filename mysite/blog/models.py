from django.conf import settings
from django.db import models
from django.utils import timezone
# 和头文件同理,链接其他代码,这样就不用把他们复制到这来

# models.Model 让django将这个类加入数据库
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # 这里面放的是 类Post 的属性

    # 类 函数(方法)

    # 构造函数 = = 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ 方法可以返回调用他的文章的标题
    def __str__(self):
        return self.title


# models.CharField   限制长度的文本
# models.TextField   无限制长度的文本
# models.DataTimeField   时间和日期
# models.ForeignKey      链接一个其他类