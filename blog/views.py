from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, RegisterForm
from .models import Post


def post_list(request):
    query = request.GET.get("q", "").strip()
    posts = Post.objects.select_related("author")
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, "blog/post_list.html", {"posts": posts, "query": query})


def post_detail(request, pk):
    return render(request, "blog/post_detail.html", {"post": get_object_or_404(Post, pk=pk)})


@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "¡Publicación creada con éxito!")
        return redirect(post)
    return render(request, "blog/post_form.html", {"form": form, "heading": "Nueva publicación"})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "Solo podés editar tus propias publicaciones.")
        return redirect(post)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Publicación actualizada.")
        return redirect(post)
    return render(request, "blog/post_form.html", {"form": form, "heading": "Editar publicación", "post": post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "Solo podés eliminar tus propias publicaciones.")
        return redirect(post)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Publicación eliminada.")
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


def register(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "¡Tu cuenta fue creada! Ya podés publicar.")
        return redirect("post_list")
    return render(request, "registration/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = AuthenticationForm
