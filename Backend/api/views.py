from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from .serializers import ExpenseSerializer

class AddExpenseView(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            # Save to Firebase
            ref = db.reference(f"users/{request.data['user_id']}/expenses")
            ref.push(serializer.validated_data)
            return Response({"message": "Expense added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetExpensesView(APIView):
    def get(self, request, user_id):
        ref = db.reference(f"users/{user_id}/expenses")
        expenses = ref.get()
        return Response(expenses, status=status.HTTP_200_OK)
