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
    hvp_date = models.DateField()
    background = models.TextField()
    licensing = models.CharField(max_length=200)
    personnel = models.ManyToManyField(User, related_name='personnel')
    representatives = models.ManyToManyField(User, related_name='representative')
    genetics_society = models.CharField(max_length=200)
    genetics_society_url = models.URLField()
    other_societies = models.ManyToManyField(Society)
    external_data = models.ManyToManyField(ExternalData)

    def __str__(self):
        return self.name


class Regulation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    regulation_text = models.TextField()

    def __str__(self):
        return self.regulation_text[:80]

    class Meta:
        abstract = True


class DNAAnalysisManager(models.Manager):
    def get_queryset(self):
        return super(DNAAnalysisManager, self).get_queryset().filter(reg_type='DNAAnalysis')


class DNAAnalysisRegulation(Regulation):
    """
    DNA analysis and interpretation practices and regulations
    in a country.

    TODO: when creating an instance, make sure reg_type is the right value
    """
    reg_type = models.CharField(max_length=32, default='DNAAnalysis', editable=False)
    objects = DNAAnalysisManager()

    class Meta:
        db_table = 'country_regulation'
        managed = True

    
class DNAStorageManager(models.Manager):
    def get_queryset(self):
        return super(DNAStorageManager, self).get_queryset().filter(reg_type='DNAStorage')


class DNAStorageRegulation(Regulation):
    """
    DNA storage practices and regulations in a country.
    """
    reg_type = models.CharField(max_length=32, default='DNAStorage', editable=False)
    objects = DNAStorageManager()

    class Meta:
        db_table = 'country_regulation'
        managed = False


class DNAReportingManager(models.Manager):
    def get_queryset(self):
        return super(DNAStorageManager, self).get_queryset().filter(reg_type='DNAReporting')


class DNAReportingRegulation(Regulation):
    """
    DNA reporting and sharing regulations in a country.
    """
    reg_type = models.CharField(max_length=32, default='DNAReporting', editable=False)
    objects = DNAReportingManager()

    class Meta:
        db_table = 'country_regulation'
        managed = False

