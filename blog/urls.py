from django.urls import path
from .views import home,article,about,article_cat,search,e404
urlpatterns = [
    path('',home),
    path('article/<str:title>',article),
    path('search',search),
    path('articles/<str:title>',article_cat),
    path('about',about),
    path('404',e404),
]
