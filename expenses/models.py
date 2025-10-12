# Django
from django.db import models
from django.contrib.auth.models import User


# Models
class ExpenseMonth(models.Model):
    """
    Montly based expense records.
    """

    expense_record_id = models.AutoField(primary_key=True)
    fk_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_months"
    )
    date = models.DateField()
