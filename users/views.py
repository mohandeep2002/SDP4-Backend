from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializers
from .models import User
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'Users List': '/user_list/',
        'Detail View': '/user_detail/<int:pk>',
        'Create': '/user_create/',
        'Update': '/user_update/',
    }

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serial = UserSerializers(users, many=True)
    return Response(serial.data)
@api_view(['POST'])
def user_create(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
