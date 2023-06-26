from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('api/get-quiz/' , views.get_quiz),
    path('quiz/' , views.quiz) 
]