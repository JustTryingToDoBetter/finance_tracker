from django.db import models

# Create your models here.
class Expense(models.Model):
    user_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()
    Expense_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Expense_name

class Budget(models.Model):
    user_id = models.CharField(max_length=255)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget_name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.budget_name