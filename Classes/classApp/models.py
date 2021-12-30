from django.db import models
from django.db.models import Model
# Create your models here.
class djangoClasses(models.Model):
    # Defines parameters for course information
    Title = models.CharField(max_length=50, default="", blank=True, null=False)
    Course_Number = models.IntegerField(max_length=50, default=0, blank=True, null=False)
    Instructor_Name = models.CharField(max_length=50, default="", blank=True, null=False)
    Duration = models.FloatField(max_length=10, default=0.00, blank=True, null=False)

    # Create model Manager
    objects = models.Manager()

    # return when an object is called
    def __str__(self):
        return self.Title

