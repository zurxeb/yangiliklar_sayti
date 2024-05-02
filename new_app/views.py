from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import News, Category

def news_list_view(request):
    news_list_slide = News.published.all()
    latest_news_5 = News.published.all()[:5]
    iqtisodiy_news_one = News.published.filter(category__nomi='Iqtisodiyot')[0]
    iqtisodiy_news_4 = News.published.filter(category__nomi='Iqtisodiyot')[0:5]
    mahalliy_news_one = News.published.filter(category__nomi='Mahalliy')[0]
    mahalliy_news_4 = News.published.filter(category__nomi='Mahalliy')[0:5]
    texnologiya_news_one = News.published.filter(category__nomi='Fan-texnika')[0]
    texnologiya_news_4 = News.published.filter(category__nomi='Fan-texnika')[0:5]
    sport_news_one = News.published.filter(category__nomi='Sport')[0]
    sport_news_4 = News.published.filter(category__nomi='Sport')[0:5]
    context = {
        'news_list': news_list_slide,
        'latest_news_5': latest_news_5,
        'iqtisodiy_news_one': iqtisodiy_news_one,
        'iqtisodiy_news_4': iqtisodiy_news_4,
        'mahalliy_news_one': mahalliy_news_one,
        'mahalliy_news_4': mahalliy_news_4,
        'texnologiya_news_one': texnologiya_news_one,
        'texnologiya_news_4': texnologiya_news_4,
        'sport_news_one': sport_news_one,
        'sport_news_4': sport_news_4,
    }

    return render(request, template_name='index.html', context=context)



def news_detail_view(request, id):

    news_detail = News.objects.get(id = id)
    yaqin_news = News.objects.filter(category__nomi=news_detail.category)[:3]
    latest_news_5 = News.published.all()[:5]
    context = {
        'news_detail': news_detail,
        'yaqin_news': yaqin_news,
        'latest_news_5': latest_news_5,
    }

    return render(request, template_name='single_page.html', context=context)

def texno_news_view(request):
    new_list = News.published.filter(category__nomi='Fan-texnika')
    latest_news_5 = News.published.all()[:5]
    context = {
        'new_list': new_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='texno.html', context=context)

def mahhal_news_view(request):
    new_list = News.published.filter(category__nomi='Mahalliy')
    latest_news_5 = News.published.all()[:5]
    context = {
        'new_list': new_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='mahhal.html', context=context)
def iqtisod_news_view(request):
    new_list = News.published.filter(category__nomi='Iqtisodiyot')
    latest_news_5 = News.published.all()[:5]
    context = {
        'new_list': new_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='iqtisod.html', context=context)
def jahon_news_view(request):
    new_list = News.published.filter(category__nomi='Dunyo')
    latest_news_5 = News.published.all()[:5]
    context = {
        'new_list': new_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='jahon.html', context=context)
def sport_news_view(request):
    new_list = News.published.filter(category__nomi='Sport')
    latest_news_5 = News.published.all()[:5]
    context = {
        'new_list': new_list,
        'latest_news_5': latest_news_5,
    }
    return render(request, template_name='sport.html', context=context)




def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse("Xabaringiz yuborildi")
    context = {
        'form' : form
    }

    return render(request, template_name='contact.html', context=context)

def about_us_view(request):
    context = {

    }

    return render(request, template_name='about.html', context=context)