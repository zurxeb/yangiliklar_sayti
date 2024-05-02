from django.urls import path
from .views import news_detail_view, news_list_view, contact_view, about_us_view, texno_news_view, mahhal_news_view, \
    iqtisod_news_view, sport_news_view, jahon_news_view

urlpatterns = [
    path('', news_list_view, name='home_page'),
    path('texnologiya/', texno_news_view, name='texno_news'),
    path('mahhaliy/', mahhal_news_view, name='mahhal_news'),
    path('iqisodiyot/', iqtisod_news_view, name='iqtisod_news'),
    path('sport/', sport_news_view, name='sport_news'),
    path('jahon/', jahon_news_view, name='jahon_news'),
    path('news/<int:id>/', news_detail_view, name='detail_page'),
    path('contact-us/', contact_view, name='contact_page'),
    path('about/', about_us_view, name='about_us_page'),

]
