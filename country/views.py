from django.shortcuts import render, get_object_or_404

from .models import Country

def detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    test_count = 345
    lab_count = 17
    return render(request, 'country/detail.html', 
        {
            'country': country,
            'test_count': test_count,
            'lab_count': lab_count,
        })
