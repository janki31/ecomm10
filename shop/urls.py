# shop app urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('basic/',views.basic,name='basic'),
    path('contact/',views.contactus,name='contact'),
    path('about/',views.about,name='about'),
    path('product/<int:pid>',views.product,name='product'),
    path('order/',views.order,name='order'),
    path('search/',views.search,name='search'),

]