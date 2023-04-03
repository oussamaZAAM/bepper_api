from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

@api_view(['GET'])
def meal_planner(request):

    # Define the calorie range for each meal
    breakfast_calories = 300
    lunch_calories = 500
    dinner_calories = 700
    snack_calories = 100

    # Define the total daily calorie goal
    daily_calories = 1800

    # Define the calorie limit for each meal
    breakfast_calorie_limit = 400
    lunch_calorie_limit = 600
    dinner_calorie_limit = 800
    snack_calorie_limit = 200

    # Define a list of meals with their calorie counts
    meals = [
        {"name": "Oatmeal with Banana and Almonds", "calories": 350},
        {"name": "Scrambled Eggs with Avocado Toast", "calories": 400},
        {"name": "Smoothie Bowl with Berries and Granola", "calories": 300},
        {"name": "Greek Yogurt with Honey and Walnuts", "calories": 250},
        {"name": "Chicken Caesar Salad", "calories": 500},
        {"name": "Turkey and Cheese Sandwich", "calories": 450},
        {"name": "Grilled Salmon with Quinoa and Roasted Vegetables", "calories": 700},
        {"name": "Pesto Pasta with Chicken and Broccoli", "calories": 800},
        {"name": "Vegetarian Chili with Cornbread", "calories": 600},
        {"name": "Hummus with Carrots and Whole Wheat Pita", "calories": 150},
        {"name": "Apple with Peanut Butter", "calories": 200},
        {"name": "Greek Yogurt with Berries", "calories": 100},
        {"name": "Hard-Boiled Egg with Whole Wheat Crackers", "calories": 150},
        {"name": "Cheese and Crackers", "calories": 250},
        {"name": "Trail Mix", "calories": 150},
        {"name": "Baked Chicken Breast with Brown Rice and Steamed Vegetables", "calories": 600},
        {"name": "Beef Stir-Fry with Mixed Vegetables and Rice Noodles", "calories": 800},
        {"name": "Grilled Portobello Mushroom Burger with Sweet Potato Fries", "calories": 650},
        {"name": "Vegetable Frittata with Whole Wheat Toast", "calories": 400},
        {"name": "Whole Wheat Pizza with Veggies and Chicken", "calories": 700},
        {"name": "Tofu and Vegetable Curry with Brown Rice", "calories": 500},
        {"name": "Shrimp and Broccoli Stir-Fry with Rice Noodles", "calories": 550},
        {"name": "Black Bean Soup with Whole Wheat Bread", "calories": 400},
        {"name": "Vegetable Stir-Fry with Tofu and Brown Rice", "calories": 600},
        {"name": "Grilled Chicken Caesar Wrap", "calories": 450},
        {"name": "Salmon and Avocado Sushi Roll", "calories": 400},
        {"name": "Roast Beef and Swiss Sandwich with Tomato Soup", "calories": 700},
        {"name": "Quinoa and Black Bean Salad with Avocado Dressing", "calories": 400},
        {"name": "Pork and Vegetable Kebabs with Couscous", "calories": 600}
    ]

    # Calculate the remaining calories for each meal
    remaining_calories = daily_calories - breakfast_calories - lunch_calories - dinner_calories - snack_calories

    # Shuffle the meal list and select meals that fit the calorie budget for each meal
    random.shuffle(meals)
    breakfast = random.choice([meal for meal in meals if breakfast_calories <= meal["calories"] <= breakfast_calorie_limit])
    lunch = random.choice([meal for meal in meals if lunch_calories <= meal["calories"] <= lunch_calorie_limit])
    dinner = random.choice([meal for meal in meals if dinner_calories <= meal["calories"] <= dinner_calorie_limit])
    snack = random.choice([meal for meal in meals if snack_calories <= meal["calories"] <= snack_calorie_limit])

    meals = [breakfast, lunch, dinner, snack]

    return Response(meals)
