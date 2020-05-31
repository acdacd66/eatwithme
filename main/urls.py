from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = "home"),
    path('new/', views.new, name="new"),
    path('board/', views.board, name="board"),
    path('detail/<int:board_id>', views.detail, name="detail"),
    path('create/', views.create, name='create'),
    path('edit/<int:board_id>', views.edit, name='edit'),
    path('update/<int:board_id>', views.update, name="update"),
    path('delete/<int:board_id>', views.delete, name="delete"),
    path('apply/<int:board_id>', views.apply, name="apply"),
]
