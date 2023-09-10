from django.db import models


# Create your models here.


class Activity(models.Model):
    check = models.BooleanField(default=False)
    subject = models.CharField(max_length = 20)
    start_date = models.DateField();
    end_date = models.DateField(null=True, blank=True)
    award = models.CharField(max_length = 5)
    content = models.CharField(max_length = 20)

    create_date = models.DateTimeField(auto_now = True)
    modify_date = models.DateTimeField(null=True, blank=True)

