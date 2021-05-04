from django.contrib import admin

# Register your models here.
from .models import Blog, WebSetting, Image_list, Text, Image, RichText, IndexPage, AboutPage, ProductsPage, \
    TechnologyPage, ContactPage


# 注册该模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'add_date', 'mod_date']


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    pass


@admin.register(WebSetting)
class SettingAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['SettingName', 'title', 'admin_sample']
    pass


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'contents', 'img']
    pass


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    # list_display = ['title', 'contents', 'img1', 'img2', 'img3']
    pass


@admin.register(ProductsPage)
class ProductsPageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    pass


@admin.register(TechnologyPage)
class TechnologyPageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    pass


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    # list_display = ['title', 'logo']
    pass


@admin.register(RichText)
class RichTextAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    # list_display = ['title', 'logo']
    pass


@admin.register(Image_list)
class SettingAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'contents', 'img']
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    # list_display = ['title', 'contents', 'img']
    pass
