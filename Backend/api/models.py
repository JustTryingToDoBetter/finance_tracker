from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models.functions import ExtractMonth, ExtractYear


class UserFinance(models.Model):
    """
    Abstract base model for finance-related entries (expenses, budgets, savings).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        abstract = True


class Expense(UserFinance):
    """
    Model for tracking user expenses.
    """
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Budget(UserFinance):
    """
    Model for tracking user budgets.
    """
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Savings(UserFinance):
    """
    Model for tracking user savings.
    """
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class Analytics:
    """
    Class for generating financial analytics for a user.
    """

    def __init__(self, user_id):
        self.user_id = user_id

    def get_total_expenses(self):
        """
        Returns the total expenses for the user.
        """
        total_expenses = Expense.objects.filter(user_id=self.user_id).aggregate(total=Sum('amount'))['total']
        return total_expenses or 0

    def get_total_budgets(self):
        """
        Returns the total budgets for the user.
        """
        total_budgets = Budget.objects.filter(user_id=self.user_id).aggregate(total=Sum('amount'))['total']
        return total_budgets or 0

    def get_total_savings(self):
        """
        Returns the total savings for the user.
        """
        total_savings = Savings.objects.filter(user_id=self.user_id).aggregate(total=Sum('amount'))['total']
        return total_savings or 0

    def get_expense_trend(self):
        """
        Returns the monthly expense trend for the user.
        """
        expenses = Expense.objects.filter(user_id=self.user_id).annotate(
            month=ExtractMonth('date'),
            year=ExtractYear('date')
        )
        expense_trend = expenses.values('month', 'year').annotate(total=Sum('amount')).order_by('year', 'month')
        return expense_trend

    def get_budget_adherence(self):
        """
        Returns the budget adherence percentage for the user.
        """
        total_budgets = self.get_total_budgets()
        total_expenses = self.get_total_expenses()

        if total_budgets == 0:
            return None

        budget_adherence = (total_expenses / total_budgets) * 100
        return budget_adherence

    def get_savings_rate(self):
        """
        Returns the savings rate percentage for the user.
        """
        total_savings = self.get_total_savings()
        total_income = self.get_total_expenses()

        if total_savings == 0:
            return None

        savings_rate = (total_savings / total_income) * 100
        return savings_rate