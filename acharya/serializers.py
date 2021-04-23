from rest_framework import serializers
from acharya.models import Courses, Subjects, Syllabus, Chapters, Exercise


class coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class syllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'
    
class chapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = '__all__'


class exerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
