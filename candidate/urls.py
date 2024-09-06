from django.urls import path
from .views import job_list_view, job_detail_view, apply_confirmation_view, applied_jobs_view, candidate_create_view,profile_view

urlpatterns = [
    path('', job_list_view, name='job_list'),  # Home page with job listings
    path('job/<int:pk>/', job_detail_view, name='job_detail'),  # Job detail view
    path('job/<int:job_id>/apply/', apply_confirmation_view, name='apply_for_job'),  # Apply for job
    path('applied-jobs/', applied_jobs_view, name='applied_jobs'),  # List of applied jobs
    path('candidate/create/', candidate_create_view, name='candidate_create'),
    path('profile/', profile_view, name='profile')  # Candidate profile creation
]
