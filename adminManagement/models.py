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

    def __str__(self):
        return self.auth_user.username


class GolfRange(models.Model):
    # golf_range_id = models.IntegerField(default=0, primary_key=True)
    golf_range_name = models.CharField(max_length=255)
    golf_range_address = models.CharField(max_length=255)
    golf_range_count = models.IntegerField(default=0)
    golf_range_staff_number = models.IntegerField(default=0)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.golf_range_name


class GolfDrivingRange(models.Model):
    # golf_range_id = models.IntegerField(default=0, primary_key=True)
    golf_range = models.ForeignKey(GolfRange, on_delete=models.CASCADE)
    range_number = models.IntegerField(default=0)
    golf_driving_range_area = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    @property
    def golf_range_name(self):
        return self.golf_range.golf_range_name

    def __str__(self):
        return "{0} driving_range_number_{1}".format(self.golf_range_name, self.range_number)


class GeographicalCoordinate(models.Model):
    # geographical_coordinate_id = models.IntegerField(default=0, primary_key=True)
    geographical_coordinate_latitude = models.DecimalField(max_digits=22, decimal_places=16, default=0)
    geographical_coordinate_longitude = models.DecimalField(max_digits=22, decimal_places=16, default=0)
    golf_driving_range = models.ForeignKey(GolfDrivingRange, on_delete=models.CASCADE)


class Robot(models.Model):
    # robot_id = models.IntegerField(default=0, primary_key=True)
    robot_name = models.CharField(max_length=255)
    note = models.CharField(max_length=255, blank=True)
    working_time = models.IntegerField(default=0)
    simulated = models.BooleanField(default=False)
    users = models.ManyToManyField(User)


class Role(models.Model):
    # role_id = models.IntegerField(default=0, primary_key=True)
    role_name = models.CharField(max_length=255)
    role_display_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, blank=True)


class Privilege(models.Model):
    # privilege_id = models.IntegerField(default=0, primary_key=True)
    privilege_name = models.CharField(max_length=255)
    role = models.ManyToManyField(Role, blank=True)
