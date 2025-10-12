# Django
from rest_framework.routers import DefaultRouter

# Views
from .views import ExpenseMonthViewSet

# Router
router = DefaultRouter()

# Routes
router.register(r"expenses", ExpenseMonthViewSet, basename="expenses")

# Urls
urlpatterns = router.urls
