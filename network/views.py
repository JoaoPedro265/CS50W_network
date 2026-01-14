from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# pagination
from django.core.paginator import Paginator

from .models import Post, User, Seguidor

from django.http import JsonResponse
from django.contrib import messages


def like_post(request):
    if request.method == "POST" and request.user.is_authenticated:
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        if request.user in post.curtidas.all():
            post.curtidas.remove(request.user)
            liked = False
        else:
            post.curtidas.add(request.user)
            liked = True

        return JsonResponse({"liked": liked, "like_count": post.curtidas.count()})

    return JsonResponse({"error": "Invalid request"}, status=400)


def index(request):
    posts = Post.objects.all().order_by("-data_criacao")
    user_paginator = Paginator(posts, 4)  # conteudo de dados e quantos dados por pagina
    page_num = request.GET.get("page")  # localizar a pagina que estou/numero da pagina
    page = user_paginator.get_page(page_num)  # pegue a page_num

    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to access this page.")
        return redirect("login")
    if "like" in request.POST:
        post_id = request.POST.get("post_id")  # Obtém o ID do post clicado
        post = get_object_or_404(Post, id=post_id)  # Busca o post no banco de dados
        if request.user in post.curtidas.all():
            post.curtidas.remove(request.user)  # Remove o like
        else:
            post.curtidas.add(request.user)  # Adiciona o like
        return redirect("index")
    return render(request, "network/index.html", {"posts": page, "user": request.user})


@login_required
def edit_post(request, post_id):
    objects = Post.objects.filter(id=post_id)
    object = objects.get(id=post_id)
    if object.autor != request.user:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect("index")
    if request.method == "POST":
        new_value = request.POST.get("value_conteudo")
        if new_value:
            object.conteudo = new_value
            object.save()
            return redirect("index")
    return render(request, "network/edit_post.html", {"objects": objects})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def following(request):
    follows = Seguidor.objects.filter(usuario=request.user)  # Pega todos os seguidore
    usuarios_seguidos = [follow.seguindo for follow in follows]
    posts = Post.objects.filter(autor__in=usuarios_seguidos).order_by("-data_criacao")
    user_paginator = Paginator(posts, 4)
    page_num = request.GET.get("page")
    page = user_paginator.get_page(page_num)
    return render(
        request,
        "network/following.html",
        {
            "posts": page,
            "user": request.user,
        },
    )


def new_post(request):  # add post
    user = request.user
    if request.method == "POST":
        if not user.is_authenticated:
            return redirect("index")
        conteu = request.POST["value_conteudo"]
        post = Post(autor=request.user, conteudo=conteu)
        post.save()
        return redirect("index")  # Redireciona para a URL nomeada 'index'
    return render(request, "network/new_post.html")


def perfil_Users(request, nome_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to access this page.")
        return redirect("login")
    users = User.objects.get(pk=nome_id)  # usuario da tabella
    print(users)
    # Verifica se o usuário logado está seguindo o usuário clicado
    is_following = Seguidor.objects.filter(
        usuario=request.user, seguindo=users
    ).exists()
    seguindo = Seguidor.objects.filter(usuario=users)
    seguidor = Seguidor.objects.filter(seguindo=users)
    posts = Post.objects.filter(autor=users).order_by("-data_criacao")
    if request.method == "POST":
        if "Follow" in request.POST:
            Seguidor.objects.create(usuario=request.user, seguindo=users)
            return redirect("perfil_Users", nome_id=nome_id)
        if "Unfollow" in request.POST:
            Seguidor.objects.filter(usuario=request.user, seguindo=users).delete()
            return redirect("perfil_Users", nome_id=nome_id)
        if "like" in request.POST:
            post_id = request.POST.get("post_id")  # Obtém o ID do post clicado
            post = get_object_or_404(Post, id=post_id)  # Busca o post no banco de dados
            if request.user in post.curtidas.all():  # Se o usuário já curtiu o post
                post.curtidas.remove(request.user)  # Remove o like
            else:
                post.curtidas.add(request.user)  # Adiciona o like
            return redirect("perfil_Users", nome_id=nome_id)
    return render(
        request,
        "network/perfil_Users.html",
        {
            "users": users,
            "seguindo": seguindo,
            "seguidor": seguidor,
            "posts": posts,
            "user": request.user,
            "is_following": is_following,
        },
    )
