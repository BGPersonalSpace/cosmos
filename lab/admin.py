from django.contrib import admin

from .models import Lab, Personnel, LabTest, Condition, GeneAnalyte, Method, Service, Certification


class PersonnelInline(admin.TabularInline): #(admin.StackedInline):
    model = Personnel
    extra = 0


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 0


class LabServiceInline(admin.TabularInline):
    model = Lab.services.through
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    inlines = [LabServiceInline]


class LabAdmin(admin.ModelAdmin):
    model = Lab
    inlines = [PersonnelInline, CertificationInline, LabServiceInline]
    exclude = ('services', )


class TestAdmin(admin.ModelAdmin):
    model = LabTest
    filter_horizontal = ('conditions', 'gene_analytes', 'methods', )

admin.site.register(Condition)
admin.site.register(GeneAnalyte)
admin.site.register(Service)
admin.site.register(Method)
admin.site.register(Lab, LabAdmin)
admin.site.register(LabTest, TestAdmin)
