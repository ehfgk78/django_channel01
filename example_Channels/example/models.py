from django.contrib.auth.models import User
from django.db import models


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        related_name='logged_in_user'
    )

