from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from categories.models import Category
from categories.serializers import CategorySerializer

from core.authentication import IsSpecialAuthenticated


class CreateCategoryView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Category Create API",
        operation_summary="Category Create API",
        request_body=CategorySerializer,
    )
    def post(self, request):
        response = {}
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'category created'
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


class AllCategoriesView(APIView):
    permission_classes = [AllowAny]

    search = openapi.Parameter(
        "search",
        in_=openapi.IN_QUERY,
        description="search artists based on their names",
        type=openapi.TYPE_STRING,
    )
    @swagger_auto_schema(
        operation_description="Get All Category API",
        operation_summary="Get All Category API",
        manual_parameters=[search]
    )
    def get(self, request):
        response = {}
        try:
            category_objs = Category.objects.all()
            if request.GET.get("search"):
                category_objs = category_objs.filter(name__icontains=request.GET.get("search"))
            serializer = CategorySerializer(category_objs, many=True)
            response['msg'] = 'categories fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Get Single Category API",
        operation_summary="Get Single Category API",
    )
    def get(self, request, id):
        response = {}
        try:
            category_obj = Category.objects.get(id=id)
            serializer = CategorySerializer(category_obj)
            response['msg'] = 'category fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Category Update API",
        operation_summary="Category Update API",
        request_body=CategorySerializer,
    )
    def put(self, request, id):
        response = {}
        try:
            category_obj = Category.objects.get(id=id)
            serializer = CategorySerializer(category_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'category updated'
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
    
    @swagger_auto_schema(
        operation_description="Delete Single Category API",
        operation_summary="Delete Single Category API",
    )
    def delete(self, request, id):
        response = {}
        try:
            Category.objects.get(id=id).delete()
            response['msg'] = 'category deleted'
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)