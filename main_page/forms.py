from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from shop import settings

from .models import Order


class OrderForm(forms.ModelForm):

    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV2Checkbox(),
    )

    def clean(self):
        if "captcha" not in self.cleaned_data:
            raise forms.ValidationError("А вы точно не робот?")

    class Meta:
        model = Order
        fields = ("name", "bike", "phone", "comment")
