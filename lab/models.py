from django.db import models
from country.models import Country


class Lab(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, null=True, blank=True)
    abbreviation = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField()
    country = models.ForeignKey(Country)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=16)
    data_sharing = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)
    gtr_lab_id = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Personnel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    role = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    date_joined = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
