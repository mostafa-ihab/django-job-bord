from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request , 'job/jobs.html', context)




def job_details(request , id ):
    job = Job.objects.get( id =id )
    context = {
        'jobs' : job
    }
    return render(request , 'job/job_details.html' , context )