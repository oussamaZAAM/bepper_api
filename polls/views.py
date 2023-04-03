from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.food import breakfastData
from polls.food import lunchData
from polls.food import dinnerData
from polls.food import snackData
import random


@api_view(['GET'])
def meal_planner(request):

    # Define the calorie range for each meal
    breakfast_calories = request.data["breakfast"][0]
    lunch_calories = request.data["lunch"][0]
    dinner_calories = request.data["dinner"][0]
    snack_calories = request.data["snack"][0]

    # Define the total daily calorie goal
    daily_calories = 1800

    # Define the calorie limit for each meal
    breakfast_calorie_limit = request.data["breakfast"][1]
    lunch_calorie_limit = request.data["lunch"][1]
    dinner_calorie_limit = request.data["dinner"][1]
    snack_calorie_limit = request.data["snack"][1]

    # Define a list of meals with their calorie counts
    breakfastMeals = breakfastData
    lunchMeals = lunchData
    dinnerMeals = dinnerData
    snackMeals = snackData
    meals = breakfastMeals + lunchMeals + dinnerMeals + snackMeals

    # Calculate the remaining calories for each meal
    remaining_calories = daily_calories - breakfast_calories - \
        lunch_calories - dinner_calories - snack_calories

    # Shuffle the meal list and select meals that fit the calorie budget for each meal
    random.shuffle(meals)
    breakfast = random.choice(
        [meal for meal in breakfastMeals if breakfast_calories <= meal["calories"] <= breakfast_calorie_limit])
    lunch = random.choice(
        [meal for meal in lunchMeals if lunch_calories <= meal["calories"] <= lunch_calorie_limit])
    dinner = random.choice(
        [meal for meal in dinnerMeals if dinner_calories <= meal["calories"] <= dinner_calorie_limit])
    snack = random.choice(
        [meal for meal in snackMeals if snack_calories <= meal["calories"] <= snack_calorie_limit])

    meals = [breakfast, lunch, dinner, snack]

    return Response(meals)
