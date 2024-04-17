from django.contrib import admin
from .models import IndividualArt, User, UserRole, Role, Permission, Module

admin.site.register(User)
admin.site.register(IndividualArt)
admin.site.register(UserRole)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Module)