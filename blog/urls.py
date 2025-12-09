from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('post/<int:pk>/partial/', views.single_post_partial, name='post_partial'),
]
