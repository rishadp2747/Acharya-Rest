from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='../media/' , blank=False, null=False)

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(blank=False, null=False)
    course = models.ForeignKey( Courses, on_delete=models.CASCADE)

