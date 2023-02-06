from django import forms
from django.db import IntegrityError

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'bike', 'phone', 'comment')