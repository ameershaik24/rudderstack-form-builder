from source_data.models import SourceFormTemplate, Source
from rest_framework import serializers


class SourceFormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceFormTemplate
        fields = "__all__"


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"
