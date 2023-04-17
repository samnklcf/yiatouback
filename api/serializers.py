from rest_framework import serializers
from api.models import Liste


class serialisatio(serializers.ModelSerializer):
    class Meta:
        model= Liste
        fields = "__all__"