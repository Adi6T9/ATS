from django.contrib import admin

# Register your models here.
from .models import JobPosting,Application

admin.site.register(JobPosting)
admin.site.register(Application)