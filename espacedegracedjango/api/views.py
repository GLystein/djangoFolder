from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import ListOfSubscribers
from .serializers import ListOfSubscribersSerializer
from .models import ListOfScripture
from .serializers import ListOfScriptureSerializer
from .serializers import StoreProductItemsSerializer
from .models import StoreProductItems
from .models import ThemeCategory
from .serializers import ThemeScriptureSerializer

# --------------------------------------------SUBSCRIBERS--------------------------------------------------------
class ListOfSubscribersCreate(generics.ListCreateAPIView):
    queryset = ListOfSubscribers.objects.all()
    serializer_class = ListOfSubscribersSerializer

class ListOfSubscribersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListOfSubscribers.objects.all()
    serializer_class = ListOfSubscribersSerializer
# --------------------------------------------S-C-R-I-P-T-U-R-E---------------------------------------------------------
# Viewing all the scripture posted by users
class ListOfScriptureCreate(generics.ListCreateAPIView):
    queryset = ListOfScripture.objects.all()
    serializer_class = ListOfScriptureSerializer

# updating Scripture API / DELETE
class ListOfScripturePostDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListOfScripture.objects.all()
    serializer_class = ListOfScriptureSerializer
    lookup_url_kwarg = 'id'

# ADDING NEW OBJECT FOR  the scripture api
class AddingScripturePosting(generics.CreateAPIView):
    queryset = ListOfScripture.objects.all()
    serializer_class = ListOfScriptureSerializer

# ---------------------------------------STORE PRODUCT ITEMS API--------------------------------------------------------
# POST METHOD API FOR PRODUCT ITEM
class StoreProductItemsCreateAPIView(generics.CreateAPIView):
    queryset = StoreProductItems.objects.all()
    serializer_class = StoreProductItemsSerializer

# VIEWING LIST OF PRODUCT ITEM
class StoreProductItemsList(generics.ListCreateAPIView):
    queryset = StoreProductItems.objects.all()
    serializer_class = StoreProductItemsSerializer


# class ListOfScripturePostUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ListOfScripturePost.objects.all()
#     serializer_class = ListOfScripturePostSerializer
#     lookup_url_kwarg = 'id'

# // create
class ThemeScripture(generics.CreateAPIView):
    queryset = ThemeCategory.objects.all();
    serializer_class = ThemeScriptureSerializer

class ThemeList(generics.ListCreateAPIView):
    queryset = ThemeCategory.objects.all();
    serializer_class = ThemeScriptureSerializer