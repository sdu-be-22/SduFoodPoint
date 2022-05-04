from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = "home"),
    path('home', index, name='home'),
    path('page/<int:pid>/', pages, name='page'), # http://127.0.0.1:8000/page/1
    path('about-us',views.abou, name='about'),
    path('account', views.account, name='account'),
    path('order', orders_page, name='orders'),
    path('menu', menu, name='menu'),
    path('info_order', info_order, name='info_order'),
    path('eat', eat),
    path('drink', drink, name = 'drink'),
    path('signin', signin, name = 'signin'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


