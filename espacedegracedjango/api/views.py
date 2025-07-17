from django.shortcuts import render
from rest_framework import generics
from .models import ListOfSubscribers
from .serializers import ListOfSubscribersSerializer
from .models import ListOfScripturePost
from .serializers import ListOfScripturePostSerializer

class ListOfSubscribersCreate(generics.ListCreateAPIView):
    queryset = ListOfSubscribers.objects.all()
    serializer_class = ListOfSubscribersSerializer

class ListOfSubscribersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListOfSubscribers.objects.all()
    serializer_class = ListOfSubscribersSerializer

class ListOfScripturePostCreate(generics.ListCreateAPIView):
    queryset = ListOfScripturePost.objects.all()
    serializer_class = ListOfScripturePostSerializer

class ListOfScripturePostDelete(generics.DestroyAPIView):
    queryset = ListOfScripturePost.objects.all()
    serializer_class = ListOfScripturePostSerializer
