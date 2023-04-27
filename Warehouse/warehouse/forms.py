import jwt
import requests

from django import forms
from core.settings import SECRET_KEY
from warehouse.models import Warehouse


class WareForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ('id', 'number', 'title', 'store', 'status')

    def save(self, commit=True):
        instance = super().save(commit=False)
        dt = {"token": 'Floship.com'}
        encode = jwt.encode(dt, SECRET_KEY, algorithm='HS256')
        headers = {"Auth": encode}
        validate_data = super().clean()
        url = 'http://127.0.0.1:8000/store/all/' 
        data = {
            "pin_cod": validate_data.get('number'),
            "title": validate_data.get('title'),
            "warehouse": validate_data.get('store'),
            "status": validate_data.get('status')
        }    
        requests.post(url=url, json=data, headers=headers)
        if commit:
            instance.save()
        return instance
