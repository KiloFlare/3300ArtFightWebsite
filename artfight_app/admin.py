from django.contrib import admin
from .models import IndividualArt, UserRole, Role, Permission, Duel

admin.site.register(IndividualArt)
admin.site.register(UserRole)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Duel)