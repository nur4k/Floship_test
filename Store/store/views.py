import jwt

from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.settings import SECRET_KEY
from store.models import Store
from store.serializers import StoreSerilizer


def decode_token(request):
    user_token: str = request.headers.get('Auth', None)
    if user_token is None:
        raise exceptions.NotAuthenticated(detail={'msg': "You do not Authenticated", }, code='403')
    valid_token = user_token.split(' ')[-1]
    secret = SECRET_KEY
    jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
    }
    decoded = jwt.decode(valid_token, secret,  algorithm='HS256', options=jwt_options)
    return decoded


class StoreView(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerilizer

    def create(self, request, *args, **kwargs):
        token = decode_token(request=request)
        token_headers = token.get('token')
        if token_headers != 'Floship.com':
            raise exceptions.AuthenticationFailed("Not auth")
        number = request.data.get('pin_cod')
        if not number:
            raise Exception("Введите пин")
        store = Store.objects.filter(pin_cod=number)
        if not store:
            store_create = Store.objects.create(**request.data)
            serializer = self.get_serializer_class()(instance=store_create) 
            return Response(data=serializer.data.data)
        store.update(**request.data)
        serializer = self.get_serializer_class()(instance=store.first())
        return Response(data=serializer.data)
