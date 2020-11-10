from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='../media/' , blank=False, null=False)

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(blank=False, null=False)
    course = models.ForeignKey( Courses, on_delete=models.CASCADE)
class Exercise(models.Model):
    mode  = models.CharField(max_length=20) #quiz,program
    question = models.TextField(default = "")
    case1 = models.CharField(max_length=100)
    case2 = models.CharField(max_length=100)
    case3 = models.CharField(max_length=100)
    case4 = models.CharField(max_length=100)
    output1 = models.CharField(max_length=100)
    output3 = models.CharField(max_length=100)
    output4 = models.CharField(max_length=100)
    output5 = models.CharField(max_length=100)
    answer = models.TextField()
    chapter = models.ForeignKey(Chapters, on_delete=models.CASCADE)
