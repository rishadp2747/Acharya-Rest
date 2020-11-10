from django.urls import path
from acharya import views

urlpatterns = [
    path('courses/', views.Courses.as_view()),
    path('subjects/', views.Subjects.as_view()),

    path('compile', views.Compile.as_view()),

    path('exercise', views.ExerciseView.as_view()),
 
]


