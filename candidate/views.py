from django.shortcuts import render, get_object_or_404, redirect
from hr.models import JobPosting, Application
from django.conf import settings
from django.contrib import messages
from .models import Candidate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def job_detail_view(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'candidate/job_detail.html', {'job': job})




def job_list_view(request):
    jobs = JobPosting.objects.all()
    return render(request, 'candidate/job_listing.html', {'jobs': jobs})

from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

@login_required
def apply_confirmation_view(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    
    try:
        candidate = Candidate.objects.get(user=request.user)
    except Candidate.DoesNotExist:
        messages.error(request, 'Please complete your profile before applying for jobs.')
        return redirect('candidate_create')

    if request.method == 'POST':
        if Application.objects.filter(candidate=candidate, job_posting=job).exists():
            messages.error(request, 'You have already applied for this job.')
            return redirect('job_list')

        application = Application(candidate=candidate, job_posting=job)
        application.save()

        # Send a confirmation email to the candidate
        try:
            send_mail(
                subject='Application Successful',
                message=f'Hello {candidate.full_name},\n\nYou have successfully applied for the position of {job.title}. We will review your application and get back to you soon.\n\nBest regards,\nGxpress',
                from_email="asnaruka2@gmail.com",
                recipient_list=[candidate.email],
                fail_silently=False,
            )
            logger.info('Confirmation email sent successfully.')
            messages.success(request, 'Your application has been submitted and a confirmation email has been sent.')
        except Exception as e:
            logger.error(f'Error sending email: {e}')
            messages.error(request, f'Your application was submitted, but there was an error sending the email: {e}')
        
        return redirect('job_list')

    return render(request, 'candidate/apply_confirmation.html', {'job': job})

    # If GET request, render confirmation template
   
 

@login_required
def applied_jobs_view(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    applications = Application.objects.filter(candidate=candidate)
    return render(request, 'candidate/applied_jobs.html', {'applications': applications})


from .forms import CandidateForm
@login_required
def candidate_create_view(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user
            candidate.save()
            messages.success(request, 'Your profile has been created.')
            return redirect('job_list')  # Redirect to job list or another relevant page
    else:
        # Pre-fill the form with the user's email
        initial_data = {'email': request.user.email}
        form = CandidateForm(initial=initial_data)
    return render(request, 'candidate/candidate_form.html', {'form': form})


@login_required
def profile_view(request):
    candidate = get_object_or_404(Candidate, user=request.user)

    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = CandidateForm(instance=candidate)

    return render(request, 'candidate/profile_view.html', {'form': form, 'candidate': candidate})
