from django.contrib import admin
from . import models

# Register your models here.


class HoodMember(admin.TabularInline):
    model = models.HoodMember


admin.site.register(models.Hood)
