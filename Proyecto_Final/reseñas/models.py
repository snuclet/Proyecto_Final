from django.db import models
from ckeditor.fields import RichTextField

class Reseña(models.Model):
    name = models.CharField(max_length=40)
    autor_reseña = models.CharField(max_length=40)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reseña: {self.name} | Autor: {self.autor_reseña}"
