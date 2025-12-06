# Django
from rest_framework.routers import DefaultRouter

# Views
from .views import (
    ExpenseTypeViewSet,
    ExpenseBudgetViewSet,
    ExpensePaymentViewSet,
    ExpenseViewSet
)

# Router
router = DefaultRouter()

# Routes
router.register(r"expenses_types", ExpenseTypeViewSet, basename="expenses_types")
router.register(r"expenses_budgets", ExpenseBudgetViewSet, basename="expenses_budgets")
router.register(r"expenses_payments", ExpensePaymentViewSet, basename="expenses_payments")
router.register(r"expenses", ExpenseViewSet, basename="expenses")


# Urls
urlpatterns = router.urls
