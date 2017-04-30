from django.db import models
from django.contrib.auth.models import User


class Society(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name


class ExternalData(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    icon = models.FileField(upload_to='projects', null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    hvp_status_choices = (
        ('Interim', 'Interim'),
    )
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=80)
    hvp_status = models.CharField(
        choices=hvp_status_choices,
        max_length=32,
        default='Interim',
    )
    hvp_date = models.DateField()
    background = models.TextField()
    standard_regulation = models.TextField()
    licensing = models.CharField(max_length=200)
    personnel = models.ManyToManyField(User, related_name='personnel')
    representatives = models.ManyToManyField(User, related_name='representative')
    genetics_society = models.CharField(max_length=200)
    genetics_society_url = models.URLField()
    other_societies = models.ManyToManyField(Society)
    external_data = models.ManyToManyField(ExternalData)
    projects = models.ManyToManyField(Project)

    dna_analysis_regulation = models.TextField()
    dna_storage_regulation = models.TextField()
    dna_reporting_regulation = models.TextField()

    def __str__(self):
        return self.name


