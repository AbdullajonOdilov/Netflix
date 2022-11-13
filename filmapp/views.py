from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class KinolarAPIView(APIView):
    def get(self,request):
        kinolar = Kino.objects.all()
        serializer = KinoSerializer(kinolar,many=True)
        return Response(serializer.data)
    def post(self,request):
        kino = request.data
        serializer = KinoSerializer(data=kino)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"true", "data":serializer.data})
        return Response({"success":"false"})

class ActorsAPIView(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors,many=True)
        return Response(serializer.data)
    def post(self,request):
        actor = request.data
        serializer = ActorSerializer(data=actor)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"true", "data":serializer.data})
        return Response({"success":"false"})

class AktorAPIView(APIView):
    def get(self,request,pk):
        actor = Actor.objects.filter(id=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    def put(self,request,pk):
        actor = Actor.objects.get(id=pk)
        serializer = ActorSerializer(actor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"info":"actor saved",'new info':serializer.data}
            return Response(natija)
        return Response({"data":"errors","detail":serializer.errors})
    def delete(self,request,pk):
        actor = Actor.objects.get(id=pk)
        actor.delete()
        return Response({"info":"actor deleted"})

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    @action(methods=["GET","POST"],detail=True)
    def commentlar(self,request,pk):
        if request.method == "POST":
            movie = Kino.objects.get(id=pk)
            comment = request.data
            serializer = CommentSerializer(data=comment)
            if serializer.is_valid():
                serializer.save(movie=movie)
                natija = {"movie": "new movie added", 'data': serializer.data}
                return Response(natija)
            return Response({'xabar': "smth went wrong!", 'detail': serializer.errors})
        comment = Comment.objects.filter(nom__id=pk)
        serializer = KinoSerializer(comment,many=True)
        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentAPIView(APIView):
    def put(self,request,pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"user": "user info saved", "added info": serializer.data}
            return Response(natija)
        return Response({"xabar": "error!"})
class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    @action(methods=['GET'],detail=True)
    def actors(self,request,pk):
        actors = Actor.objects.filter(ism__id=pk)
        serializer = ActorSerializer(actors,many=True)
        return Response(serializer.date)



