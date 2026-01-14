from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("new_post", views.new_post, name="new_post"),
    path("<int:nome_id>/", views.perfil_Users, name="perfil_Users"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("like/", views.like_post, name="like_post"),
]
