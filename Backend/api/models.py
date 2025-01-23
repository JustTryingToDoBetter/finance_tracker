from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models.functions import ExtractMonth, ExtractYear


# Create your models here.
class UserFinance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        abstract = True

class Expense(UserFinance):
    Expense_name = models.TextField(null=True, blank=True)

class Budget(UserFinance):
    Budget_name = models.TextField(null=True, blank=True)

class Savings(UserFinance):
    Savings_name = models.TextField(null=True, blank=True)
    

class Analytics:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_total_expenses(self):
        total_expenses = Expense.objects.filter(user_id=self.user_id).aggregate(Sum('amount'))['amount__sum']
        return total_expenses

    def get_total_budgets(self):
        total_budgets = Budget.objects.filter(user_id=self.user_id).aggregate(Sum('budget_amount'))['budget_amount__sum']
        return total_budgets

    def get_total_savings(self):
        total_savings = Savings.objects.filter(user_id=self.user_id).aggregate(Sum('amount'))['amount__sum']
        return total_savings

    def get_expense_trend(self):
        expenses = Expense.objects.filter(user_id=self.user_id).annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
        expense_trend = expenses.values('month', 'year').annotate(total=Sum('amount')).order_by('year', 'month')
        return expense_trend

    def get_budget_adherence(self):
        budgets = Budget.objects.filter(user_id=self.user_id)
        total_budgets = budgets.aggregate(Sum('budget_amount'))['budget_amount__sum']
        total_expenses = Expense.objects.filter(user_id=self.user_id).aggregate(Sum('amount'))['amount__sum']
        if total_budgets == 0:
            return None
        else:
            budget_adherence = (total_expenses / total_budgets) * 100
        
        return budget_adherence

    def get_savings_rate(self):
        savings = Savings.objects.filter(user_id=self.user_id)
        total_savings = savings.aggregate(Sum('amount'))['amount__sum']
        total_income = Expense.objects.filter(user_id=self.user_id).aggregate(Sum('amount'))['amount__sum']
        if total_savings == 0:
            return None
        else:
            savings_rate = (total_income / total_savings) * 100
        return savings_rate