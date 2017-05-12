from django.shortcuts import render, get_object_or_404

from .models import Lab

def lab_detail(request, lab_id):
    lab = get_object_or_404(Lab, pk=lab_id)
    return render(request, 'lab/detail.html', 
        {
            'lab': lab,
        })
