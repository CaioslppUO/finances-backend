# Django
from rest_framework.routers import DefaultRouter

# Views
from .views import (
    ExpenseMonthViewSet,
    ExpenseTypeViewSet,
    ExpenseBudgetViewSet,
    ExpensePaymentViewSet,
)

# Router
router = DefaultRouter()

# Routes
router.register(r"expenses", ExpenseMonthViewSet, basename="expenses")
router.register(r"expenses_types", ExpenseTypeViewSet, basename="expenses_types")
router.register(r"expenses_budgets", ExpenseBudgetViewSet, basename="expenses_budgets")
router.register(
    r"expenses_payments", ExpensePaymentViewSet, basename="expenses_payments"
)


# Urls
urlpatterns = router.urls
