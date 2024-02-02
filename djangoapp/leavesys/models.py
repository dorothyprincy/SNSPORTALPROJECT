from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#leave
# from django.db import models
# from django.contrib.auth.models import User

LEAVE_TYPE_CHOICES = [
    ('Paid', 'Paid Leave'),
    ('Unpaid', 'Unpaid Leave'),
    ('Sick', 'Sick Leave'),
]
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

class LeaveRequest(models.Model):
    """
    A leave request made by an employee.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    message = models.TextField(blank=True)

    def _str_(self):
        """
        Returns a string representation of the leave request.
        """
        return f'{self.user} - {self.leave_type} - {self.start_date} to {self.end_date}'

EMPLOYEE_CHOICES = [(user.id, user.get_full_name()) for user in User.objects.all()]

def get_leave_request(user):
    """
    Returns the leave requests made by a user, sorted by start date in descending order.
    """
    return LeaveRequest.objects.filter(user=user).order_by('-start_date')