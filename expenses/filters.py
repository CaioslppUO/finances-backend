# Django
import django_filters

# Models
from expenses.models import Expense

class ExpenseFilter(django_filters.FilterSet):
    # O filtro 'month' usa o lookup_expr='month' no campo date do ExpenseMonth
    month = django_filters.NumberFilter(
        field_name='date', 
        lookup_expr='month', 
        label='Mês para filtragem (1-12)'
    )
    year = django_filters.NumberFilter(
        field_name='date', 
        lookup_expr='year', 
        label='Ano para filtragem (Ex: 2024)'
    )
    
    class Meta:
        model = Expense
        fields = ['month', 'year']