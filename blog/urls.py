from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserLoginView, post_create, post_delete, post_detail, post_list, post_update, register

urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/nuevo/", post_create, name="post_create"),
    path("post/<int:pk>/editar/", post_update, name="post_update"),
    path("post/<int:pk>/eliminar/", post_delete, name="post_delete"),
    path("registro/", register, name="register"),
    path("ingresar/", UserLoginView.as_view(), name="login"),
    path("salir/", LogoutView.as_view(), name="logout"),
]
