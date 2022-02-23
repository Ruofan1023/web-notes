from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("allnote", views.allnote, name="allnote"),
    path("archive", views.archive, name="archive"),
    path("lock/<noteid>", views.lock, name="lock"),
    path("unlock/<noteid>", views.unlock, name="unlock"),
]
