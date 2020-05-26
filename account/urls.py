from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout ,name="logout"),
    path('mypage/',views.mypage ,name="mypage"),
    path('edit/<int:user_id>', views.edit, name="edit"),
    path('update/<int:user_id>',views.update, name="update"),
]
