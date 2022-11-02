from django.db import models

class Equipo(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    #description = RichTextField(null=True, blank=True)
    

    def __str__(self):
        return f"Nombre: {self.name} {self.last_name}"