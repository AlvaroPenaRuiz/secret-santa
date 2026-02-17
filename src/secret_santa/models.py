from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image_url = models.CharField(max_length=255, blank=True, null=True)

class Edition(models.Model):
    class Status(models.TextChoices):
            UPCOMING = "upcoming", "Upcoming"
            ACTIVE = "active", "Active"
            COMPLETED = "completed", "Completed"

    class Privacy(models.TextChoices):
            PUBLIC = "public", "Public"
            PRIVATE = "private", "Private"
            EXAMPLE = "example", "Example"
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.UPCOMING)
    privacy = models.CharField(max_length=50, choices=Privacy.choices, default=Privacy.PUBLIC)
    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    considerations = models.TextField(blank=True, null=True)
    participants_excluded = models.ManyToManyField("self", blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GiftImage(models.Model):
    id = models.AutoField(primary_key=True)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name="images")
    image_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Assignment(models.Model):
    id = models.AutoField(primary_key=True)

    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    giver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="giver")
    receiver = models.ForeignKey(Participant,  null=True, on_delete=models.CASCADE, related_name="receiver")
    gift = models.ForeignKey(Gift, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)