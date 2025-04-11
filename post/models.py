from django.db import models


# Modelo base
class Post(models.Model):
    pass


# Subclase: Post de texto
class TextPost(Post):
    pass


# Subclase: Post con imagen
class ImagePost(Post):
    pass
