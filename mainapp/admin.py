from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from mainapp.models import CustomUser, AdminHOD, Staff, Users


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staff)
admin.site.register(Users)

