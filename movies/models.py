from django.db import models

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'filmler/') 

    def __str__(self):
        return self.name 