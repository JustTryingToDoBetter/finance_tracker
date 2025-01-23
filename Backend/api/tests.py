from django.test import TestCase
from django.contrib.auth.models import User
from .models import Expense, Budget, Savings, Analytics


class UserFinanceModelTests(TestCase):
    def setUp(self):
        """
        Set up test data for all tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_expense_creation(self):
        """
        Test that an expense can be created.
        """
        expense = Expense.objects.create(
            user=self.user,
            amount=100.0,
            category="Food",
            date="2023-10-15",
            name="Lunch at a restaurant"
        )
        self.assertEqual(expense.amount, 100.0)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.name, "Lunch at a restaurant")

    def test_budget_creation(self):
        """
        Test that a budget can be created.
        """
        budget = Budget.objects.create(
            user=self.user,
            amount=500.0,
            category="Groceries",
            date="2023-10-01",
            name="Monthly grocery budget"
        )
        self.assertEqual(budget.amount, 500.0)
        self.assertEqual(budget.category, "Groceries")
        self.assertEqual(budget.name, "Monthly grocery budget")

    def test_savings_creation(self):
        """
        Test that savings can be created.
        """
        savings = Savings.objects.create(
            user=self.user,
            amount=200.0,
            category="Emergency Fund",
            date="2023-10-01",
            name="Emergency savings"
        )
        self.assertEqual(savings.amount, 200.0)
        self.assertEqual(savings.category, "Emergency Fund")
        self.assertEqual(savings.name, "Emergency savings")

class AnalyticsTests(TestCase):
    def setUp(self):
        """
        Set up test data for all tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.analytics = Analytics(user_id=self.user.id)

        # Create test expenses
        Expense.objects.create(user=self.user, amount=100.0, category="Food", date="2023-10-15", name="Lunch")
        Expense.objects.create(user=self.user, amount=200.0, category="Transport", date="2023-10-16", name="Bus fare")

        # Create test budgets
        Budget.objects.create(user=self.user, amount=500.0, category="Groceries", date="2023-10-01", name="Monthly budget")

        # Create test savings
        Savings.objects.create(user=self.user, amount=300.0, category="Emergency Fund", date="2023-10-01", name="Savings")

    def test_get_total_expenses(self):
        """
        Test the total expenses calculation.
        """
        total_expenses = self.analytics.get_total_expenses()
        self.assertEqual(total_expenses, 300.0)

    def test_get_total_budgets(self):
        """
        Test the total budgets calculation.
        """
        total_budgets = self.analytics.get_total_budgets()
        self.assertEqual(total_budgets, 500.0)

    def test_get_total_savings(self):
        """
        Test the total savings calculation.
        """
        total_savings = self.analytics.get_total_savings()
        self.assertEqual(total_savings, 300.0)

    def test_get_expense_trend(self):
        """
        Test the expense trend calculation.
        """
        expense_trend = self.analytics.get_expense_trend()
        self.assertEqual(len(expense_trend), 1)  # Only one month of data
        self.assertEqual(expense_trend[0]['total'], 300.0)  # Total for October 2023

    def test_get_budget_adherence(self):
        """
        Test the budget adherence calculation.
        """
        budget_adherence = self.analytics.get_budget_adherence()
        self.assertAlmostEqual(budget_adherence, 60.0)  # (300 / 500) * 100

    def test_get_savings_rate(self):
        """
        Test the savings rate calculation.
        """
        savings_rate = self.analytics.get_savings_rate()
        self.assertAlmostEqual(savings_rate, 100.0)  # (300 / 300) * 100