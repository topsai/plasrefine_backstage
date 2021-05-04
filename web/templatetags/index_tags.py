from django import template
from web.models import Blog, Image_list, WebSetting
from django.conf import settings

register = template.Library()

# 自定义新闻列表显示数量
list_count = 4


# 注册自定义简单标签
@register.simple_tag
def get_news4_tag():
    news4 = Blog.objects.order_by('-id')[:list_count]
    print("news4", news4)
    return news4


@register.simple_tag
def get_settings():
    print(settings.WEBSETTING_INDEX)
    set = WebSetting.objects.filter(id=settings.WEBSETTING_INDEX).first()
    print(set)
    return set
# {% load index_tags %}
