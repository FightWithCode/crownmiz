from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.authentication import IsSpecialAuthenticated
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from artists.models import Artist
from artists.serializers import ArtistSerializer


class CreatArtistView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Artist Create API",
        operation_summary="Artist Create API",
        request_body=ArtistSerializer,
    )
    def post(self, request):
        response = {}
        try:
            serializer = ArtistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'artist created'
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
    

class AllArtistView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    search = openapi.Parameter(
        "search",
        in_=openapi.IN_QUERY,
        description="search artists based on their names",
        type=openapi.TYPE_STRING,
    )
    @swagger_auto_schema(
        operation_description="Get All Artist API",
        operation_summary="Get All Artist API",
        manual_parameters=[search]
    )
    def get(self, request):
        response = {}
        try:
            artist_objs = Artist.objects.all()
            if request.GET.get("search"):
                artist_objs = artist_objs.filter(name__icontains=request.GET.get("search"))
            serializer = ArtistSerializer(artist_objs, many=True)
            response['msg'] = 'artists fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ArtistView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Get Single Artist API",
        operation_summary="Get Single Artist API",
    )
    def get(self, request, id):
        response = {}
        try:
            artist_objs = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artist_objs)
            response['msg'] = 'artist fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Artists Update API",
        operation_summary="Artists Update API",
        request_body=ArtistSerializer,
    )
    def put(self, request, id):
        response = {}
        try:
            artist_objs = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artist_objs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'artist updated'
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
        operation_description="Delete Single Artist API",
        operation_summary="Delete Single Artist API",
    )
    def delete(self, request, id):
        response = {}
        try:
            Artist.objects.get(id=id).delete()
            response['msg'] = 'artist deleted'
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)