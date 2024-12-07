from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from AUTH.models import CustomerUser
from .serializers import CustomUserSerializer  # Assuming you have this serializer
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def user_registration(request):
    data = request.data

    # Check if the email already exists
    if CustomerUser.objects.filter(email=data['email']).exists():
        return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Serialize the data
    serializer = CustomUserSerializer(data=data)

    # Validate and save the data
    if serializer.is_valid():
        serializer.save()
        user=CustomerUser
        user = CustomerUser.objects.get(email=data['email'])
        token =Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def user_login(request):
    data = request.data
    
    try:
        user = CustomerUser.objects.get(email=data['email'])
    except CustomerUser.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Check if password matches
    if not user.check_password(data['password']):
        return Response({'detail': 'Invalid password.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # If valid, authenticate and return a token (optional)
    token, created = Token.objects.get_or_create(user=user)

    # Return success response with token
    return Response({
        'message': 'Login successful!',
        'token': token.key
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def test_token(request):

    return Response({})  
