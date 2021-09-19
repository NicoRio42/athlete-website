from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:article_slug>/', views.article, name='article'),
    path('thanks/', views.thanks, name='thanks'),
]