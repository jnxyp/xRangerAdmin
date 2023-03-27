from django.contrib import admin

from adminManagement.models import User, Robot, GolfRange, Role, Privilege, GolfDrivingRange, GeographicalCoordinate


class UserAdmin(admin.ModelAdmin):
    list_display = ('auth_user',)


admin.site.register(User, UserAdmin)


class GolfRangeAdmin(admin.ModelAdmin):
    list_display = ('golf_range_name',)


admin.site.register(GolfRange, GolfRangeAdmin)


class GolfDrivingRangeAdmin(admin.ModelAdmin):
    list_display = ('get_driving_golf_range', 'range_number', 'pk')

    @admin.display(ordering='golf_range__golf_range_name', description='golf_range_name')
    def get_driving_golf_range(self, obj):
        return obj.golf_range_name


admin.site.register(GolfDrivingRange, GolfDrivingRangeAdmin)


class GeographicalCoordinateAdmin(admin.ModelAdmin):
    list_display = ('get_golf_range', 'get_golf_driving_range_number', 'pk')

    @admin.display(ordering='golf_range__golf_range_name', description='golf_range_name')
    def get_golf_range(self, obj):
        return obj.golf_driving_range.golf_range.golf_range_name

    @admin.display(ordering='golf_range__golf_range_name', description='range_number')
    def get_golf_driving_range_number(self, obj):
        return obj.golf_driving_range.range_number


admin.site.register(GeographicalCoordinate, GeographicalCoordinateAdmin)


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
