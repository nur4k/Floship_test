import jwt
import requests

from django import forms
from core.settings import SECRET_KEY
from store.models import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ("id", "pin_cod", "title", "status", "warehouse")

    def save(self, commit=True):
        dt = {"token": 'Floship.com'}
        encode = jwt.encode(dt, SECRET_KEY, algorithm='HS256')
        headers = {"Auth": encode}
        instance = super().save(commit=False)
        validate_data = super().clean()
        url = 'http://127.0.0.1:8001/warehouse/add/'
        data = {
            "number": validate_data.get('pin_cod'),
            "title": validate_data.get('title'),
            "store": validate_data.get('warehouse'),
            "status": validate_data.get('status')
        }
        requests.post(url=url, json=data, headers=headers)
        if commit:
            instance.save()
        return instance
