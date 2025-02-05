from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from .serializers import ExpenseSerializer, BudgetSerializer, SavingsSerializer
import firebase_admin
from firebase_admin import credentials, auth


if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\Cowin\OneDrive - University of the Western Cape\Documents\GitHub\finance_tracker\Backend\Backend\financetracker-2e8d5-firebase-adminsdk-fbsvc-8e51af60fb.json")
    firebase_admin.initialize_app(cred)


class FirebaseLoginView(View):
    @csrf_exempt
    def post(self, request):
        # Extract the Firebase token from the request header
        firebase_token = request.headers.get('Authorization')
        
        if not firebase_token:
            return JsonResponse({"error": "No token provided"}, status=400)
        
        try:
            # Verify the Firebase token
            decoded_token = auth.verify_id_token(firebase_token)
            user_id = decoded_token['uid']
            
            # Now you can either create a new user in your DB or retrieve an existing one
            # For example, create a user record
            # User.objects.get_or_create(firebase_uid=user_id)
            
            return JsonResponse({"message": "User authenticated successfully", "user_id": user_id}, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
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


class GetExpensesView(BaseFinanceView):
    """ 

    Retrieves all expenses for a specific user.
    """

    def __init__(self):
        super().__init__(ExpenseSerializer, "expenses")

class GetBudgetsView(BaseFinanceView):
    """
    Retrieves all budgets for a specific user.
    """

    def __init__(self):
        super().__init__(BudgetSerializer, "expenses")
        
class GetSavingsView(BaseFinanceView):
    """
    Retrieves all savings for a specific user.
    """

    def __init__(self):
        super().__init__(SavingsSerializer, "expenses")


def Home(request):
    return JsonResponse({"message": "Welcome!"}, status=200)

def Auth(request):
    return JsonResponse({"message": "You're logged in."}, status=200)