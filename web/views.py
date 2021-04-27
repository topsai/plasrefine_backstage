from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'services.html')


def technology(request):
    return render(request, 'technology.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    # data = Blog.objects.all()
    return render(request, 'news.html')


def news_detail(request, blog_id=None):
    data = None
    # if blog_id:
    #     data = Blog.objects.filter(id=blog_id)
    return render(request, 'web/news_detail.html', {"data": data})


def gallery(request):
    return render(request, 'web/gallery.html')


def hongna(request):
    return render(request, 'web/hongna.html')


def hongna_cn(request):
    return render(request, 'web_cn/hongna.html')


def hongda(request):
    return render(request, 'web/hongda.html')


def hongda_cn(request):
    return render(request, 'web_cn/hongda.html')


#  cn
def home_cn(request):
    return render(request, 'web_cn/index.html')


def advance_aerogel_cn(request):
    return render(request, 'web_cn/advance_aerogel.html')


def advance_aerogel_grow_cn(request):
    return render(request, 'web_cn/advance_aerogel_grow.html')


def advance_aerogel(request):
    return render(request, 'web/advance_aerogel.html')


def aerogels_we_provide_cn(request):
    return render(request, 'web_cn/aerogels_we_provide.html')


def aerogels_we_provide(request):
    return render(request, 'web/aerogels_we_provide.html')


def advance_aerogel_grow(request):
    return render(request, 'web/advance_aerogel_grow.html')


def service_cn(request):
    return render(request, 'web_cn/services.html')


def about_cn(request):
    return render(request, 'web_cn/about.html')


def contact_cn(request):
    return render(request, 'web_cn/contact.html')


def news_cn(request):
    data = Blog.objects.all()
    return render(request, 'web_cn/typo.html', {"data": data})


def news_detail_cn(request, blog_id=None):
    data = None
    if blog_id:
        data = Blog.objects.filter(id=blog_id)
    return render(request, 'web_cn/news_detail.html', {"data": data})


def gallery_cn(request):
    return render(request, 'web_cn/gallery.html')
