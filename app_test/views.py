from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from .token import get_tokens
from django.contrib.auth.models import User
# Create your views here.


class HomeApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'message':'success'})
    
class LoginApiView(APIView):
    def post(self,request):
        if not request.data:
            return Response({'error': 'No data provided.', 'detail': 'Provide a valid data'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username = username , password = password)
        token = get_tokens(user)
        return Response({'message':'sucess','token':token})


class RegisterApiView(APIView):
    def post(self,request):
        if not request.data:
            return Response({'error': 'No data provided.', 'detail': 'Provide a valid data'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create(username = username,password = password)
        user.save()
        data = {
            'username':user.username
        }
        return Response({'messge':'account successfully created','payload':data})