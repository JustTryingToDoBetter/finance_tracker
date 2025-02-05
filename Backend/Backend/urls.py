"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin

from django.urls import path, include
from api.views import (
    AddExpenseView,
    GetExpensesView,
    DeleteExpenseView,
    AddBudgetView,
    GetBudgetsView,
    AddSavingsView,
    GetSavingsView,
    FirebaseLoginView,
    Auth,
    Home
)

# API URL patterns
api_urlpatterns = [
    # Expense endpoints
    path('expenses', AddExpenseView.as_view(), name='add-expense'),
    path('expenses/<str:user_id>', GetExpensesView.as_view(), name='get-expenses'),
    path('expenses/<str:user_id>/<str:expense_id>', DeleteExpenseView.as_view(), name='delete-expense'),

    # Budget endpoints
    path('budgets', AddBudgetView.as_view(), name='add-budget'),
    path('budgets/<str:user_id>', GetBudgetsView.as_view(), name='get-budgets'),

    # Savings endpoints
    path('savings', AddSavingsView.as_view(), name='add-savings'),
    path('savings/<str:user_id>', GetSavingsView.as_view(), name='get-savings'),

    # Firebase login endpoint
    path('login', FirebaseLoginView.as_view(), name='firebase-login'),


    # Auth endpoints
    path('auth', Auth, name='auth'),
    path('home', Home, name='home'),
]

# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),  # Include API URLs under the 'api/' prefix
]