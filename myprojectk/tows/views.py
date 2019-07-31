from django.shortcuts import render
from tows.models import Crane, Pilot, Assignment
# Create your views here.


def show_assignment(request):
    num_cranes = Crane.objects.all().count()
    num_pilots = Pilot.objects.count()
    num_assignments = Assignment.objects.all().count()
    num_assignments_available = Assignment.objects.filter(status__exact='a').count()

    context = {
        'num_cranes': num_cranes,
        'num_pilots': num_pilots,
        'num_assignments': num_assignments,
        'num_assignments_available': num_assignments_available,
    }
    return render(request, 'tows/page.html', context=context)
