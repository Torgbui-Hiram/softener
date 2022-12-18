from django.db import models
from django.conf import settings
from django.utils import timezone


class FabricSoftener(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image_url = models.CharField(max_length=2083, blank=True, null=True)
    price = models.FloatField(max_length=2083)
    stock = models.IntegerField()
    product_volume = models.CharField(max_length=10, default='500ML')
    product_image = models.ImageField(
        editable=True, blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name


class Traders(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default='admin')
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=25)
    country = models.CharField(max_length=50)
    proof_id = models.CharField(max_length=35)
    email = models.CharField(max_length=40)
    profile_picture = models.ImageField(
        editable=True, blank=True, null=True, upload_to='profile/')
    signup_date = models.DateTimeField(default=timezone.now)


def __str__(self):
    return self.title
