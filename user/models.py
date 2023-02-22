from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
# Create your models here.
# oluşturan : foreignkey (manytoone)
# isim 
# resim
class Profile(models.Model):
    id = models.UUIDField(primary_key = True, db_index=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='İsim')
    image = models.FileField(upload_to = 'profiles/', verbose_name='Resim')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, editable=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super().save(*args, **kwargs)


class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to= 'hesap/') 
    telefon  = models.IntegerField()

    def __str__(self):
        return self.user.username     