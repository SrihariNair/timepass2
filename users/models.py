from datetime import datetime, date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    M='M'
    F='F'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    SEC_CHOICE =(
        ('Whats your pet name', 'Whats your pets name'),
        ('Whats your best friends name', 'Whats your best frens name'),
        ('How old are you', 'How old are you'),
    )
    security_question=models.CharField(max_length=200,choices=SEC_CHOICE)

    birth_date = models.DateField(("Birth Date"), default=date.today)

    answer=models.CharField(blank=True, max_length=255)

    resume=models.FileField()

    image=models.ImageField(blank=True, null=True,upload_to="media%Y%m%d/")


    def __str__(self):
        return self.username

class userPosts(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    APPROVE_CHOICE = (
        ('APPROVED', 'APPROVED'),
        ('NOT APPROVED', 'NOT APPROVED'),
    )
    approval = models.CharField(blank=True, max_length=100, choices=APPROVE_CHOICE)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject)

