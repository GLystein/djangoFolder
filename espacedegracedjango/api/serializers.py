from rest_framework import serializers
from .models import ListOfSubscribers
from .models import ListOfScripture
from .models import StoreProductItems
from .models import ThemeCategory
from .models import UpcomingEvents

class ListOfSubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfSubscribers
        fields = ["id", "firstName", "lastName", "email","subscribType", "startedDate"]

class ListOfScriptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfScripture
        fields = ["id", "author","topic", "category", "date", "message"]

class StoreProductItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProductItems
        fields = '__all__'

class ThemeScriptureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeCategory
        fields = '__all__'

class UpcomingEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvents
        fields = '__all__'