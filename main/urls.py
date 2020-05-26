from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = "home"),
    path('new/', views.new, name="new"),
    path('board/', views.board, name="board"),
    path('detail/<int:board_id>', views.detail, name="detail"),
    path('create/', views.create, name='create'),
]
