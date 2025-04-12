from django.db import models


# Modelo base
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)

    POST_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES)

    def __str__(self):
        return self.title


# Subclase: Post de texto
class TextPost(Post):
    content = models.TextField()

    def save(self, *args, **kwargs):
        self.post_type = 'text'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.content[:20]}..."


# Subclase: Post con imagen
class ImagePost(Post):
    image = models.ImageField(upload_to='media/post/images/')

    def save(self, *args, **kwargs):
        self.post_type = 'image'
        super().save(*args, **kwargs)
