from rest_framework import serializers
from .models import Expense, Budget, Savings


class BaseFinanceSerializer(serializers.ModelSerializer):
    """
    Base serializer for finance-related models to avoid code duplication.
    """

    class Meta:
        abstract = True
        fields = '__all__'


class ExpenseSerializer(BaseFinanceSerializer):
    """
    Serializer for the Expense model.
    """

    class Meta(BaseFinanceSerializer.Meta):
        model = Expense


class BudgetSerializer(BaseFinanceSerializer):
    """
    Serializer for the Budget model.
    """

    class Meta(BaseFinanceSerializer.Meta):
        model = Budget


class SavingsSerializer(BaseFinanceSerializer):
    """
    Serializer for the Savings model.
    """

    class Meta(BaseFinanceSerializer.Meta):
        model = Savings