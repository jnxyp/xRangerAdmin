from django.contrib import admin

from adminManagement.models import User, Robot, GolfRange, Role, Privilege


class UserAdmin(admin.ModelAdmin):
    list_display = ('auth_user',)


admin.site.register(User, UserAdmin)


class GolfRangeAdmin(admin.ModelAdmin):
    list_display = ('golf_range_name',)


admin.site.register(GolfRange, GolfRangeAdmin)


class RobotAdmin(admin.ModelAdmin):
    list_display = ('robot_name',)


admin.site.register(Robot, RobotAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)


admin.site.register(Role, RoleAdmin)


class PrivilegeAdmin(admin.ModelAdmin):
    list_display = ('privilege_name',)


admin.site.register(Privilege, PrivilegeAdmin)

# Register your models here.
