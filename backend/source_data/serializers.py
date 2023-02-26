from source_data.models import SourceFormTemplate, Source
from rest_framework import serializers


class SourceFormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceFormTemplate
        fields = "__all__"


class SourceSerializer(serializers.ModelSerializer):
    source_form = serializers.SerializerMethodField()

    class Meta:
        model = Source
        fields = "__all__"

    def get_source_form(self, obj):
        return obj.source_form_template.source_form
