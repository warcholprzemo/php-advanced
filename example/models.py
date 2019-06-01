from django.db import models


class GiftList(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    guests = models.IntegerField()

    def __str__(self):
        return f'{self.name} for {self.guests} guests'


class Gift(models.Model):
    name = models.CharField(max_length=128)
    gift_list = models.ForeignKey(GiftList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
