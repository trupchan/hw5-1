from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from .models import UserConfirmation
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

@api_view(['POST'])
def confirm_user(request):
    code = request.data.get('code')
    if not code:
        return Response({'error': 'Code is required'}, status=400)
    try:
        confirmation = UserConfirmation.objects.get(code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User confirmed'})
    except UserConfirmation.DoesNotExist:
        return Response({'error': 'Invalid code'}, status=400)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})