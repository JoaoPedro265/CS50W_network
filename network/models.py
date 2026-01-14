from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.id}:{self.autor.username}: {self.conteudo[:30]}"


class Seguidor(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="seguidores"
    )
    seguindo = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="seguindo"
    )

    def __str__(self):
        return f"{self.usuario} segue-> {self.seguindo}"
