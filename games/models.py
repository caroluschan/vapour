from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

# Create your models here.


class Genre(models.Model):
	name = models.CharField(max_length=250)

class Tag(models.Model):
	name = models.CharField(max_length=250)

class Game(models.Model):
	name = models.CharField(max_length=250)
	developer = models.CharField(max_length=250)
	genre = models.ForeignKey(Genre, default=1)
	tag = models.ManyToManyField(Tag)
	price = models.FloatField(default=0)
	windows= models.BooleanField(default=False)
	mac = models.BooleanField(default=False)
	linux = models.BooleanField(default=False)
	short_description = models.TextField(blank=True, null=True)
	long_description = models.TextField(blank=True, null=True)

class Reward(models.Model):
	user = models.ForeignKey(User, default=1)
	amount = models.FloatField(default=0)
	start_date = models.DateTimeField(auto_now_add=True, blank=True)
	expiry = models.DateTimeField(blank=True) #need to be revised

class AccSpending(models.Model): #clear
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	spending = models.FloatField(default=0)

class Purchase(models.Model):
	time = models.DateTimeField(auto_now_add=True, blank=True)
	user = models.ForeignKey(User, default=1)
	game = models.ForeignKey(Game, default=1)
	reward_used = models.FloatField(default=0)

class UserBalance(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.FloatField(default=0)

class UserAvatar(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)
	avatar = models.FileField()
	

# @receiver(post_save, sender=User)
# def create_user_avatar(sender, instance, created, **kwargs):
#     if created:
#         UserAvatar.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_avatar(sender, instance, **kwargs):
#     instance.useravatar.save()

