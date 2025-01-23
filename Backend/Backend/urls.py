"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import AddExpenseView, GetExpensesView,DeleteExpenseView, AddBudgetView,GetBudgetsView, AddSavingsView,GetSavingsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/expenses', AddExpenseView.as_view()),
    path('api/expenses/<str:user_id>', GetExpensesView.as_view()),
    path('api/expenses/<str:user_id>/<str:expense_id>', DeleteExpenseView.as_view()),
    path('api/budgets', AddBudgetView.as_view()),
    path('api/budgets/<str:user_id>', GetBudgetsView.as_view()),
    path('api/savings', GetSavingsView.as_view()),
    path('api/savings/<str:user_id>', AddSavingsView.as_view())
]

