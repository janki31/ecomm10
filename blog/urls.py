# blog app urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('blogpost/<int:bid>', views.blogpost, name='blogpost'),

]