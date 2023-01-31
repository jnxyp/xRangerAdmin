from django.contrib import admin

from adminManagement.models import User, Robot, GolfRange, Role, Privilege

admin.site.register(User)
admin.site.register(GolfRange)
admin.site.register(Robot)
admin.site.register(Role)
admin.site.register(Privilege)

# Register your models here.
