from django.db import models
from django.forms import ModelForm
# Create your models here.
from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import django.utils.timezone as timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe


# 博客模型
class Blog(models.Model):
    title = models.CharField("标题", max_length=100, unique=False)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    contents = RichTextUploadingField("内容")
    introduction = models.CharField("简介", max_length=300)
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
    # imgpic_640x427 = ProcessedImageField(
    #     upload_to='DF_goods/Image/%Y/%m',
    #     processors=[ResizeToFill(640, 427)],
    #     format='JPEG',
    #     options={'quality': 90},
    #     verbose_name="图片"
    # )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'COMMUNITY/FAQS'
        verbose_name_plural = 'COMMUNITY/FAQS'


# 基础设置
class WebSetting(models.Model):
    SettingName = models.CharField(max_length=60, verbose_name="配置名称")
    title = models.CharField(max_length=60, verbose_name="网站名称")
    phone = models.CharField(max_length=60,verbose_name='电话')
    email = models.CharField(max_length=60,verbose_name='邮箱')
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    # content = RichTextUploadingField()
    # introduction = models.CharField("简介", max_length=60)
    # time = models.DateTimeField(default=timezone.now)
    # add_date = models.DateTimeField('保存日期', default=timezone.now)
    # mod_date = models.DateTimeField('最后修改日期', auto_now=True)
    logo = models.ImageField(help_text="LOGO 分辨率:180*55", upload_to='Image/logo')
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
    # logo = ProcessedImageField(
    #     upload_to='DF_goods/Image/%Y/%m',
    #     processors=[ResizeToFill(180, 55)],
    #     format='PNG',
    #     options={'quality': 90},
    #     verbose_name="LOGO"
    # )

    # 列表显示图片方法,return 返回的是图片的地址
    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="55" width="150" />' % self.logo)

    admin_sample.short_description = 'Logo'
    admin_sample.allow_tags = True

    #
    def __str__(self):
        return self.SettingName

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


# 轮播图
class Image_list(models.Model):
    title = models.CharField("标题", max_length=30)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    contents = models.CharField("内容", max_length=30)
    # 方式二:
    img = ProcessedImageField(
        upload_to='DF_goods/Image/%Y/%m',
        processors=[ResizeToFill(1920, 750)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 首页
class IndexPage(models.Model):
    title = models.CharField("标题", max_length=100)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    contents = models.CharField("内容", max_length=200)
    # 方式二:
    img = ProcessedImageField(
        upload_to='Image/index',
        processors=[ResizeToFill(1920, 750)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class ContactPage(models.Model):
    title = models.CharField("标题", max_length=30)
    # 方式二:
    img = ProcessedImageField(
        upload_to='Image/contact',
        processors=[ResizeToFill(600, 450)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contact'


# About 页
class AboutPage(models.Model):
    title = models.CharField("标题", max_length=30)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    contents = RichTextUploadingField("内容")
    # 方式二:
    img1 = ProcessedImageField(
        upload_to='Image/about',
        processors=[ResizeToFill(960, 640)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片1"
    )
    img2 = ProcessedImageField(
        upload_to='Image/about',
        processors=[ResizeToFill(960, 640)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片2"
    )
    img3 = ProcessedImageField(
        upload_to='Image/about',
        processors=[ResizeToFill(960, 720)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片3"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'


# technology
class TechnologyPage(models.Model):
    title = models.CharField("标题", max_length=30)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    list = models.ManyToManyField("Text")
    contents1 = RichTextUploadingField("内容1")
    # 方式二:
    img1 = ProcessedImageField(
        upload_to='Image/technology',
        processors=[ResizeToFill(1440, 375)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片1"
    )
    contents2 = RichTextUploadingField("内容2")
    img2 = ProcessedImageField(
        upload_to='Image/technology',
        processors=[ResizeToFill(600, 300)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片2"
    )
    img3 = ProcessedImageField(
        upload_to='Image/technology',
        processors=[ResizeToFill(500, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片3"
    )
    img4 = ProcessedImageField(
        upload_to='Image/technology',
        processors=[ResizeToFill(500, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片4"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technology'


# products
class ProductsPage(models.Model):
    text1 = models.CharField("文本1", max_length=30)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    # 方式二:
    img1 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片1"
    )
    img2 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片2"
    )
    img3 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片3"
    )
    img4 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片4"
    )
    text2 = models.CharField("文本1", max_length=30)
    # 博客的内容为 RichTextField 对象
    # body = RichTextField()  # 这个不能上传图片
    # 方式二:
    img5 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片1"
    )
    img6 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片2"
    )
    img7 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片3"
    )
    img8 = ProcessedImageField(
        upload_to='Image/product',
        processors=[ResizeToFill(550, 350)],
        format='JPEG',
        options={'quality': 90},
        verbose_name="图片4"
    )

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'


# 单行文本
class Text(models.Model):
    contents = models.CharField("内容", max_length=200)

    def __str__(self):
        return self.contents

    class Meta:
        verbose_name = '文本'
        verbose_name_plural = '文本'


# 多行文本
class RichText(models.Model):
    contents = RichTextUploadingField("内容")

    def __str__(self):
        return self.contents

    class Meta:
        verbose_name = '富文本'
        verbose_name_plural = '富文本'


# 图片
class Image(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '图片'
