from django.contrib import admin

from .models import Lab, Personnel


class PersonnelInline(admin.TabularInline): #(admin.StackedInline):
    model = Personnel
    extra = 0


class LabAdmin(admin.ModelAdmin):
    model = Lab
    inlines = [PersonnelInline]

admin.site.register(Lab, LabAdmin)
