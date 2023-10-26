from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.models import Movie, Song
from core.serializers import MovieSerializer, SongSerializer
from core.authentication import IsSpecialAuthenticated



class CreatMovieView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Movie Create API",
        operation_summary="Movie Create API",
        request_body=MovieSerializer,
    )
    def post(self, request):
        response = {}
        try:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'movie created'
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
    

class AllMovieView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    search = openapi.Parameter(
        "search",
        in_=openapi.IN_QUERY,
        description="search movie based on their names",
        type=openapi.TYPE_STRING,
    )
    @swagger_auto_schema(
        operation_description="Get All Movies API",
        operation_summary="Get All Movies API",
        manual_parameters=[search]
    )
    def get(self, request):
        response = {}
        try:
            movies_objs = Movie.objects.all()
            if request.GET.get("search"):
                movies_objs = movies_objs.filter(name__icontains=request.GET.get("search"))
            serializer = MovieSerializer(movies_objs, many=True)
            response['msg'] = 'movies fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Get Single Movie API",
        operation_summary="Get Single Movie API",
    )
    def get(self, request, id):
        response = {}
        try:
            movies_objs = Movie.objects.get(id=id)
            serializer = MovieSerializer(movies_objs)
            response['msg'] = 'movie fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Movie Update API",
        operation_summary="Movie Update API",
        request_body=MovieSerializer,
    )
    def put(self, request, id):
        response = {}
        try:
            movies_objs = Movie.objects.get(id=id)
            serializer = MovieSerializer(movies_objs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'movie updated'
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
        operation_description="Delete Single Movie API",
        operation_summary="Delete Single Movie API",
    )
    def delete(self, request, id):
        response = {}
        try:
            Movie.objects.get(id=id).delete()
            response['msg'] = 'movie deleted'
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        

class CreatSongView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Song Create API",
        operation_summary="Song Create API",
        request_body=SongSerializer,
    )
    def post(self, request):
        response = {}
        try:
            serializer = SongSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'song created'
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
    

class AllSongView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    search = openapi.Parameter(
        "search",
        in_=openapi.IN_QUERY,
        description="search songs based on their names",
        type=openapi.TYPE_STRING,
    )
    musician = openapi.Parameter(
        "musician",
        in_=openapi.IN_QUERY,
        description="search songs based on their musician",
        type=openapi.TYPE_STRING,
    )
    lyricist = openapi.Parameter(
        "lyricist",
        in_=openapi.IN_QUERY,
        description="search songs based on their lyricist",
        type=openapi.TYPE_STRING,
    )
    @swagger_auto_schema(
        operation_description="Get All Song API",
        operation_summary="Get All Song API",
        manual_parameters=[search, musician, lyricist]
    )
    def get(self, request):
        response = {}
        try:
            song_objs = Song.objects.all()
            if request.GET.get("search"):
                song_objs = song_objs.filter(name__icontains=request.GET.get("search"))
            if request.GET.get("musician"):
                song_objs = song_objs.filter(musician__name__icontains=request.GET.get("musician"))
            if request.GET.get("lyricist"):
                song_objs = song_objs.filter(lyricist__name__icontains=request.GET.get("lyricist"))
            serializer = SongSerializer(song_objs, many=True)
            response['msg'] = 'song fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class SongView(APIView):
    permission_classes = [IsSpecialAuthenticated]

    @swagger_auto_schema(
        operation_description="Get Single Song API",
        operation_summary="Get Single Song API",
    )
    def get(self, request, id):
        response = {}
        try:
            song_objs = Song.objects.get(id=id)
            serializer = SongSerializer(song_objs)
            response['msg'] = 'song fetched'
            response['data'] = serializer.data
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Song Update API",
        operation_summary="Song Update API",
        request_body=SongSerializer,
    )
    def put(self, request, id):
        response = {}
        try:
            song_objs = Song.objects.get(id=id)
            serializer = SongSerializer(song_objs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['msg'] = 'song updated'
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
        operation_description="Delete Single Song API",
        operation_summary="Delete Single Song API",
    )
    def delete(self, request, id):
        response = {}
        try:
            Song.objects.get(id=id).delete()
            response['msg'] = 'song deleted'
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response["msg"] = "error"
            response["error"] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)