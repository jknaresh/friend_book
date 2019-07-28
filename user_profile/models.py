from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserFriend(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user id")
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="friend id", related_name="friend_id")

    c_on = models.DateTimeField(editable=False, auto_now_add=True)
    u_on = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        unique_together = (("user_id", "friend_id"),)
        ordering = ["-u_on"]

    def __str__(self):
        return f"{self.user_id.username} - {self.friend_id.username}"
