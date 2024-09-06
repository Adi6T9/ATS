from django.shortcuts import render
from visits.models import PageVisit
from hr.models import JobPosting,Application


def home(request,*args,**kwargs):
    title="Home"
    job_postings = JobPosting.objects.all()
    application=Application.objects.all()
    visits = PageVisit.objects.all()
    context = {
        'visits': visits,
        'job_postings': job_postings,
        'applications': application,
    }
    return render(request, 'base.html', context)