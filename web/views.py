from django.shortcuts import render
from web.models import Blog, Image_list, IndexPage, AboutPage, TechnologyPage, ProductsPage, ContactPage
from functools import wraps
import functools


def use_logging(func):
    @functools.wraps(func)
    def _deco(*args, **kwargs):
        print("%s is running" % func.__name__)
        func(*args, **kwargs)

    return _deco


def get_4new_list():
    news4 = Blog.objects.all()[:4]
    return news4


# Create your views here.
def home(request):
    images = IndexPage.objects.all()
    return render(request, 'index.html', {"images": images})


def service(request):
    return render(request, 'services.html')


def technology(request):
    data = TechnologyPage.objects.first()
    print(data.title)
    print(data.list.all())
    return render(request, 'technology.html', {"data": data})


def about(request):
    data = AboutPage.objects.first()
    return render(request, 'about.html', {"data": data})


def products(request):
    data = ProductsPage.objects.first()
    return render(request, 'products.html', {"data": data})


def contact(request):
    data = ContactPage.objects.first()
    return render(request, 'contact.html', {"data": data})


def news(request):
    data = Blog.objects.order_by('-id')
    return render(request, 'news.html', {"data": data, })


def news_detail(request, blog_id=None):
    data = None
    if blog_id:
        data = Blog.objects.filter(id=blog_id).first()
        print("-->", data.files.url)
    else:
        print('none')
    return render(request, 'viewer.html', {"data": data})
