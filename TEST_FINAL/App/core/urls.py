from django.urls import path

from . import views

urlpatterns = [
    path('home', views.Home, name="Home"),

    path('profile/register/', views.Register, name="register"),
    path('profile/loging/', views.login, name="login"),
    path('profile/logout/', views.logout_page, name="logout"),

    path('profile/create/<int:pk>/', views.Create_Profile, name="create-profile"),
    path('profile/edit/<int:pk>/', views.Profile_Edit, name="edit-profile"),

    path('profile/OverView/<int:pk>/', views.Profile_View, name="profile"),

    path('home/post/detail/<int:pk>/', views.Post_Detail, name="post-detail"),
    path('home/post/add/', views.Add_Post, name="add-post"),
    path('home/post/edit/<int:pk>/', views.Post_Edit, name="post-edit"),
    path('home/post/delete/<int:pk>/', views.Post_Delete, name="post-delete"),

    path('home/post/comment/edit/<int:pk>/', views.Comment_Edit, name="comment-edit"),
    path('home/post/comment/delete/<int:pk>/', views.Comment_Delete, name="comment-delete"),

]