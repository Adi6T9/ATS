from django.db import models
from requisition.models import Requisition
from candidate.models import Candidate
from ckeditor.fields import RichTextField



class JobPosting(models.Model):
    id = models.AutoField(primary_key=True)
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    posted_date = models.DateField()

    class Meta:
        ordering = ['posted_date']  # Default order by posted_date

    def __str__(self):
        return self.title


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-application_date']  # Default order by application_date, descending

    def __str__(self):
        return f'{self.candidate.full_name} - {self.job_posting.title}'