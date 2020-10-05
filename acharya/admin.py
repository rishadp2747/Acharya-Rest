from django.contrib import admin
from .models import Courses, Subjects,Syllabus,Chapters,Exercise

# Register your models here.
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Syllabus)
admin.site.register(Chapters)
admin.site.register(Exercise)

