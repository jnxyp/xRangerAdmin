from django.db import models
from django.conf import settings


class User(models.Model):
    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_id = models.IntegerField(default=0)
    # username = models.CharField(max_length=255)
    # password_hash = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=255)


class GolfRange(models.Model):
    golf_range_id = models.IntegerField(default=0)
    golf_range_name = models.CharField(max_length=255)
    golf_range_address = models.CharField(max_length=255)
    golf_range_area = models.IntegerField(default=0)
    golf_range_staff_number = models.IntegerField(default=0)
    users = models.ManyToManyField(User)


class Robot(models.Model):
    robot_id = models.IntegerField(default=0)
    robot_name = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    working_time = models.IntegerField(default=0)
    users = models.ManyToManyField(User)


class Role(models.Model):
    role_id = models.IntegerField(default=0)
    role_name = models.CharField(max_length=255)
    role_display_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)


class Privilege(models.Model):
    privilege_id = models.IntegerField(default=0)
    privilege_name = models.CharField(max_length=255)
    role = models.ManyToManyField(Role)
