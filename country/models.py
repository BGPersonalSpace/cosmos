from django.db import models
from django.contrib.auth.models import User


class Society(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()


class ExternalData(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()


class Country(models.Model):
    hvp_status_choices = (
        ('Interim', 'Interim'),
    )

    name = models.CharField(max_length=200)
    region = models.CharField(max_length=80)
    hvp_status = models.CharField(
        max_length=32,
        choices=hvp_status_choices,
        default='Interim',
    ),
    date = models.DateField('hvp date')
    background = models.TextField()
    licensing = models.CharField(max_length=200)
    personnel = models.ManyToManyField(User, related_name='personnel')
    representatives = models.ManyToManyField(User, related_name='representative')
    genetics_society = models.CharField(max_length=200)
    genetics_society_url = models.URLField()
    other_societies = models.ManyToManyField(Society)
    external_data = models.ManyToManyField(ExternalData)


class DNAAnalysisRegulation(models.Model):
    """
    DNA analysis and interpretation practices and regulations
    in a country.

    Alternatively, model inheritance can be used for all regulations.
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    regulation_text = models.TextField()

    
class DNAStorageRegulation(models.Model):
    """
    DNA storage practices and regulations in a country.

    Alternatively, model inheritance can be used for all regulations.
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    regulation_text = models.TextField()


class DNAReportingRegulation(models.Model):
    """
    DNA reporting and sharing regulations in a country.

    Alternatively, model inheritance can be used for all regulations.
    """
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    regulation_text = models.TextField()


