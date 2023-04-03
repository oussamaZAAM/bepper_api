from django.urls import path

from . import views

urlpatterns = [
    path('meal-planner/', views.meal_planner, name='meal_planner'),
]