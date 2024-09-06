from django.contrib.auth.models import User
from django.db import models

class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    applied_jobs = models.ManyToManyField(
        'hr.JobPosting',
        through='hr.Application',
        related_name='applicants'
    )
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['full_name']  # Default order by full_name

    def __str__(self):
        return self.full_name

