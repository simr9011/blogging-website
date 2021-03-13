from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('blog',views.blog),
    path('blogpost/<int:id>',views.blogpost),
    path('home',views.home),
    path('add/',views.addblog.as_view()),
    path('search/',views.search)

]

