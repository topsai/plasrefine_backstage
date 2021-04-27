from django.db import models
from django.forms import ModelForm
# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import django.utils.timezone as timezone

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


# 博客模型
class Blog(models.Model):
    title = models.CharField("标题", max_length=30, unique=False)

    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    content = RichTextUploadingField()
    introduction = models.CharField("简介", max_length=60)
    # time = models.DateTimeField(default=timezone.now)
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    # img = models.ImageField()
    # imgpic_30x30 = ImageSpecField(
    #     # 原图
    #     source='img',
    #     # 处理后的图像大小
    #     processors=[ResizeToFill(30, 30)],
    #     # 处理后的图片格式
    #     format='JPEG',
    #     # 处理后的图片质量
    #     options={'quality': 90}
    # )
    # 方式二:
    imgpic_640x427 = ProcessedImageField(
        upload_to='DF_goods/Image/%Y/%m',
        processors=[ResizeToFill(640, 427)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'


# 基础设置
class Setting(models.Model):
    title = models.CharField("网站名称", max_length=30, unique=False)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    # content = RichTextUploadingField()
    # introduction = models.CharField("简介", max_length=60)
    # time = models.DateTimeField(default=timezone.now)
    # add_date = models.DateTimeField('保存日期', default=timezone.now)
    # mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    # img = models.ImageField()
    # imgpic_30x30 = ImageSpecField(
    #     # 原图
    #     source='img',
    #     # 处理后的图像大小
    #     processors=[ResizeToFill(30, 30)],
    #     # 处理后的图片格式
    #     format='JPEG',
    #     # 处理后的图片质量
    #     options={'quality': 90}
    # )
    # 方式二:
    logo = ProcessedImageField(
        upload_to='DF_goods/Image/%Y/%m',
        processors=[ResizeToFill(180, 55)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="LOGO"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = '网站设置'
