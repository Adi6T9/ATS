from django.db import models
from django.contrib.auth.models import User

class Requisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    req_id = models.AutoField(primary_key=True)
    Department = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    num_positions = models.PositiveIntegerField()
    level = models.CharField(max_length=100)
    kra = models.TextField()
    location = models.CharField(max_length=100)
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    urgency = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']  # Default order by created_at, descending

    def __str__(self):
        return f'{self.req_id} - {self.Department} - {self.Designation}'
