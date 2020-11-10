from rest_framework import serializers
from acharya.models import Courses, Subjects
from acharya.models import Exercise

class coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class exerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
