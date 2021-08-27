from rest_framework import serializers
from expenses.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('category',
                  'title',
                  'title',
                  'price')


class ExpenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('category',
                  'title',
                  'title',
                  'price',
                  'account',
                  'date_created')
        depth = 1
