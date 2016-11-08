from django.contrib import admin
from django import forms
from django.contrib.auth.models import User, Group
from .custom_admin_site import Mysite

from django.contrib.admin import AdminSite

from .models import (
    Part,
    PartSide,
    DecalCategory,
    Decal,
    PartSideDecal,
)


@admin.register(Part, PartSide, Decal, site=Mysite)
class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Part)
admin.site.register(PartSideDecal)
admin.site.register(PartSide)
admin.site.register(Decal)
admin.site.register(DecalCategory)
