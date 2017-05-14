from django.shortcuts import render, get_object_or_404

from .models import Lab, LabTest
from country.models import Country

def lab_detail(request, lab_id):
    lab = get_object_or_404(Lab, pk=lab_id)
    return render(request, 'lab/detail.html', 
        {
            'lab': lab,
        })


def labs_by_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'lab/country_labs.html', 
        {
            'country': country,
            'labs': country.lab_set.all(),
        })


def tests_by_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'lab/country_tests.html',
        {
            'country': country,
            'tests': LabTest.objects.filter(lab__country_id=country_id),
        })
