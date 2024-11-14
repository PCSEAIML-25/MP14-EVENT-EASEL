from django.db import models
from datetime import date

# Create your models here.


class recruitments(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email_personal = models.EmailField(null=False, blank=False)
    email_kiet = models.EmailField(null=False, blank=False)
    library_id = models.CharField(max_length=50, null=False, blank=False)
    contact_no = models.CharField(max_length=15, null=False, blank=False)
    day_scholar_hosteller = models.CharField(
        max_length=15, null=False, blank=False)
    gender = models.CharField(max_length=50, null=False, blank=False)
    branch = models.CharField(max_length=15, null=False, blank=False)
    payment_mode = models.CharField(max_length=15, null=False, blank=False)
    desk = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateTimeField(default=date.today)
    payment_status = models.BooleanField(default=False)
    recruitment_mail=models.BooleanField(default=False)

    def _str_(self):
        return self.name
