from django.db import models

# Create your models here.
job_type ={
  (  'Full Time','Full Time'),
    ('Part Time','Part Time')
} 

class Job(models.Model):
    title = models.CharField(max_length=70)
    #location
    job_type = models.TextField(max_length=50,choices=job_type) 
    description = models.TextField(max_length=1000)
    publish_at = models.DateTimeField(auto_now=True )
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)

    def __str__(self):
        return self.title    