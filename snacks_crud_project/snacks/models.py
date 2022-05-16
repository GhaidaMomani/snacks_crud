from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Snack(models.Model):
    title = models.CharField(max_length=255)
    number = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    purchaser = models.IntegerField(default=0)
    description = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_snack', kwargs={"pk":self.pk})