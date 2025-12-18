from rest_framework import serializers
from .models import SubscribersList
from .models import ScriptureList, LastestEpisodes
from .models import StoreProductItems
from .models import ThemeCategory
from .models import UpcomingEvents
from .models import SlideshowsImage
from .models import UpcomingEvents

class SubscribersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribersList
        # fields = ["id", "firstName", "lastName", "email","subscribType", "startedDate"]
        fields = '__all__'

class ScriptureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptureList
        # fields = ["id", "author","topic", "category", "date", "message"]
        fields = '__all__'

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
class SlideshowsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideshowsImage
        fields = '__all__'
class LastestEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestEpisodes
        fields = '__all__'
class EventsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvents
        fields = '__all__'