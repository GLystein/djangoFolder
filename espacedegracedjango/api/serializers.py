from rest_framework import serializers
from .models import ListOfSubscribers
from .models import ListOfScripturePost

class ListOfSubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfSubscribers
        fields = ["id", "firstName", "lastName", "email","subscribType", "startedDate"]

class ListOfScripturePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfScripturePost
        fields = ["id", "author","topic", "category", "date", "message"]