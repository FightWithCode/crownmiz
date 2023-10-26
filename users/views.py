from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.shortcuts import render

from users.models import User
from users.serializers import UserSerializer


class UsersRegistrationView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="User Register API",
        operation_summary="User Register API",
        request_body=UserSerializer,
    )
    def post(self, request):
        response = {}
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'user created'
                response['data'] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                response["msg"] = "error"
                response["error"] = serializer.errors
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        response = {}
        try:
            user_obj = User.objects.get(id=id)
            serializer = UserSerializer(user_obj)
            response['msg'] = 'user fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="User Update API",
        operation_summary="User Update API",
        request_body=UserSerializer,
    )
    def put(self, request, id):
        response = {}
        try:
            user_obj = User.objects.get(id=id)
            if User.objects.filter(username=request.data.get("username")):
                response["msg"] = "error"
                response["error"] = "Username already exists!"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=request.data.get("email")):
                response["msg"] = "error"
                response["error"] = "Email already exists!"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            serializer = UserSerializer(user_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                if request.data.get('password'):
                    user_obj.set_password(request.data.get('password'))
                    user_obj.save()
                response['msg'] = 'user updated'
                response['data'] = serializer.data
                return Response(response, status=status.HTTP_200_OK)
            else:
                response["msg"] = "error"
                response["error"] = serializer.errors
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        response = {}
        try:
            User.objects.get(id=id).delete()
            response['msg'] = 'user deleted'
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
