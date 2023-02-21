from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import permission_classes
from rest_framework.response import Response#
from rest_framework_simplejwt.authentication import JWTAuthentication
#from django.contrib.auth.models import group
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Create your views here.

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    ordering_fields = {'price', 'inventory'}
    filterset_fields = {'price', 'inventory'}
    search_fields = ['note_name']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    #@permission_classes([IsAuthenticated])
    def get_permissions(self):
        return [IsAuthenticated()]
        #return Response({'message':'Some secret messages'})

class Manager(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    #manager_group = Group.objects.get(name='Manager')
    #staff_group = Group.objects.get(name='Staff')
    
    def get(self, request):
        
        if request.user.groups.filter(name='Manager').exists():
            return Response({'message':'Only for the Manager view'})
        elif request.user.groups.filter(name='Staff').exists():
            return Response({'message':'Only for the staff and manager view only'})
        else:
            return Response({'message':'You are not authorized'})

        
    
        
class SingleNoteView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer