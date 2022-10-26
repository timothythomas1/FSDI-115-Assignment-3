
from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms
from django.contrib.auth.models import Group
from django.conf import settings

# Now create a custom migration for status to communicate to. 
# We are not putting this into the Status class due to later maintainability concerns. (Refactoring?)
class Post(models.Model):
    body = models.TextField()
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True, 
        blank=True
    )
    # created_on = models.DateTimeField(default=datetime.now)
#     poster = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#  # django will create a different name to avoid collisions when running > python3 manage.py makemigrations
#     )

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('post_detail', args=[self.id])
# Create your models here.



