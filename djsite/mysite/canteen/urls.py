from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('home', index, name='home'),
    path('page/<int:pid>/', pages, name='page'), # http://127.0.0.1:8000/page/1
    path('about-us', about, name='about'),
    path('account', account, name='account'),
    path('order', orders_page, name='orders'),
    path('menu', menu, name='menu'),
    path('info_order', info_order, name='info_order'),
    path('eat', eat),
    path('drink', drink, name = 'drink'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


