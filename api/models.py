from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)  # g, kg, quả, ml...

    calories = models.FloatField()
    carb = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Tuần 1, Tiệc sinh nhật...
    start_date = models.DateField()
    end_date = models.DateField()

class MealPlanItem(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField()
class FoodInventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class ShoppingItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    is_purchased = models.BooleanField(default=False)

# Create your models here.
