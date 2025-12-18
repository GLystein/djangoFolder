from django.shortcuts import render
from rest_framework import generics,viewsets, parsers
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import LastestEpisodes
from .models import SubscribersList
from .serializers import LastestEpisodesSerializer
from .serializers import SubscribersListSerializer
from .models import ScriptureList
from .serializers import ScriptureListSerializer
from .serializers import StoreProductItemsSerializer
from .models import StoreProductItems
from .models import ThemeCategory
from .serializers import ThemeScriptureSerializer
from .serializers import UpcomingEventsSerializer
from .models import UpcomingEvents
from .models import SlideshowsImage
from .serializers import SlideshowsImageSerializer
from .models import  SubscribersList

# record_to_delete = SubscribersList.objects.get(id=1)
SubscribersList.objects.all().delete()
# record_to_delete.delete()
# --------------------------------------------SUBSCRIBERS--------------------------------------------------------
class SubscribersListCreate(generics.ListCreateAPIView):
    queryset = SubscribersList.objects.all()
    serializer_class = SubscribersListSerializer

class SubscribersListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscribersList.objects.all()
    serializer_class = SubscribersListSerializer
# --------------------------------------------S-C-R-I-P-T-U-R-E---------------------------------------------------------
# Viewing all the scripture posted by users
class ScriptureListCreate(generics.ListCreateAPIView):
    queryset = ScriptureList.objects.all()
    serializer_class = ScriptureListSerializer

# updating Scripture API / DELETE
class ScripturePostDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScriptureList.objects.all()
    serializer_class = ScriptureListSerializer
    lookup_url_kwarg = 'id'

# ADDING NEW OBJECT FOR  the scripture api
class AddingScripturePosting(generics.CreateAPIView):
# class AddingScripturePosting(viewsets.ModelViewSet):
    queryset = ScriptureList.objects.all()
    serializer_class = ScriptureListSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)

# ---------------------------------------STORE PRODUCT ITEMS API--------------------------------------------------------
# POST METHOD API FOR PRODUCT ITEM
# class StoreItems(generics.CreateAPIView): # need to change this to ListCreateAPIView
class StoreItems(generics.ListCreateAPIView):
    queryset = StoreProductItems.objects.all()
    serializer_class = StoreProductItemsSerializer

# Store Items Deletion
class ItemsDeletion(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreProductItems.objects.all()
    serializer_class = StoreProductItemsSerializer
    lookup_url_kwarg = 'id'

# VIEWING LIST OF PRODUCT ITEM
# class ItemsDetails(generics.ListCreateAPIView):
#     queryset = StoreProductItems.objects.all()
#     serializer_class = StoreProductItemsSerializer


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

# ---------------------------------------UpComing Events API--------------------------------------------------------

# class GetUpcomingEvents(generics.CreateAPIView):
class GetUpcomingEvents(generics.ListCreateAPIView):
    queryset = UpcomingEvents.objects.all();
    serializer_class = UpcomingEventsSerializer

class EventsUpdate(generics.RetrieveUpdateDestroyAPIView):
# class EventsDeletion(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingEvents.objects.all();
    serializer_class = UpcomingEventsSerializer

# ---------------------------------------Slideshow API--------------------------------------------------------
class SlideList(generics.ListCreateAPIView):
    queryset = SlideshowsImage.objects.all();
    serializer_class = SlideshowsImageSerializer

class SlideShowPost(generics.CreateAPIView):
    queryset = SlideshowsImage.objects.all();
    serializer_class = SlideshowsImageSerializer

class slideShowDeletion(generics.RetrieveUpdateDestroyAPIView):
    queryset = SlideshowsImage.objects.all();
    serializer_class = SlideshowsImageSerializer


#-------------------------------------Last Episode--------------------------------------------------------------
class LastestEpisodesList(generics.RetrieveUpdateDestroyAPIView):
# class LastestEpisodesList(generics.ListCreateAPIView):
    queryset = LastestEpisodes.objects.all();
    serializer_class = LastestEpisodesSerializer