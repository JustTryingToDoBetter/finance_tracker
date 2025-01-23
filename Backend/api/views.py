from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from .serializers import ExpenseSerializer, BudgetSerializer, SavingsSerializer


class BaseFinanceView(APIView):
    """
    Base class for finance-related views to avoid code duplication.
    """

    def __init__(self, serializer_class, firebase_path):
        self.serializer_class = serializer_class
        self.firebase_path = firebase_path

    def post(self, request):
        """
        Handles POST requests to add a new finance entry (expense, budget, or savings).
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            ref = db.reference(f"users/{request.data['user_id']}/{self.firebase_path}")
            ref.push(serializer.validated_data)
            return Response({"message": f"{self.firebase_path.capitalize()} added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        """
        Handles GET requests to retrieve all finance entries for a user.
        """
        ref = db.reference(f"users/{user_id}/{self.firebase_path}")
        entries = ref.get()
        return Response(entries, status=status.HTTP_200_OK)


class AddExpenseView(BaseFinanceView):
    """
    View for adding and retrieving expenses.
    """

    def __init__(self):
        super().__init__(ExpenseSerializer, "expenses")


class AddBudgetView(BaseFinanceView):
    """
    View for adding and retrieving budgets.
    """

    def __init__(self):
        super().__init__(BudgetSerializer, "budgets")


class AddSavingsView(BaseFinanceView):
    """
    View for adding and retrieving savings.
    """

    def __init__(self):
        super().__init__(SavingsSerializer, "savings")


class DeleteExpenseView(APIView):
    """
    View for deleting a specific expense.
    """

    def delete(self, request, user_id, expense_id):
        """
        Handles DELETE requests to delete an expense by its ID.
        """
        ref = db.reference(f"users/{user_id}/expenses/{expense_id}")
        ref.delete()
        return Response({"message": "Expense deleted successfully!"}, status=status.HTTP_200_OK)