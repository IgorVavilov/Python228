from django.shortcuts import render
from .models import Jobs

def index(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})
