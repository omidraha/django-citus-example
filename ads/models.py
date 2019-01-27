from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=512)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Campaign(models.Model):
    class Meta:
        unique_together = (('id', 'company'),)

    name = models.CharField(max_length=512)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Ads(models.Model):
    class Meta:
        unique_together = (('id', 'company'),)

    name = models.CharField(max_length=512)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks_count = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

