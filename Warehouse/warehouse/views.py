import jwt

from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.settings import SECRET_KEY
from warehouse.models import Warehouse
from warehouse.serializers import WareSerializer


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
    decoded = jwt.decode(valid_token, secret, algorithms=['HS256'], options=jwt_options)
    return decoded

class WareView(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WareSerializer

    def create(self, request, *args, **kwargs):
        token = decode_token(request=request)
        token_headers = token.get('token')
        if token_headers != 'Floship.com':
            raise exceptions.AuthenticationFailed("Not auth")
        pin_cod = request.data.get('number')
        if not pin_cod:
            raise Exception("Введите номер")
        warehose = Warehouse.objects.filter(number=pin_cod)
        if not warehose:
            warehose_create = Warehouse.objects.create(**request.data)
            serializer = self.get_serializer_class()(instance=warehose_create) 
            return Response(data=serializer.data)
        warehose.update(**request.data)
        serializer = self.get_serializer_class()(instance=warehose.first())
        return Response(data=serializer.data)
