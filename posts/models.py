from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.core.exceptions import ValidationError


# Modelo base
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    content = models.TextField()

    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title


class FeaturedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_featured=True)


class FeaturedPost(Post):
    objects = FeaturedManager()

    def highlight(self):
        return f"🌟 {self.title.upper()} 🌟"

    class Meta:
        proxy = True


class Comment(BaseModel):
    user = models.CharField(max_length=100)
    content = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    ALLOWED_MODELS = ['post']

    def clean(self):
        if self.content_type.model not in self.ALLOWED_MODELS:
            raise ValidationError(
                f"No se permite asociar comentarios con el modelo {self.content_type.model}")

    def __str__(self):
        return f"Comentario de {self.user} sobre {self.content_object}"
