from django.http import JsonResponse
from rest_framework import generics
from source_data.serializers import SourceFormTemplateSerializer, SourceSerializer
from source_data.models import SourceFormTemplate, Source
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_source_types(request):
    # return only those source types for which form template is present
    form_templates_source_types = SourceFormTemplate.objects.values_list("source_type", flat=True)

    response = {
        source_type: getattr(SourceFormTemplate.SourceType, source_type).label
        for source_type in form_templates_source_types
    }

    return JsonResponse(response)

class SourceFormTemplateList(generics.CreateAPIView):
    serializer_class = SourceFormTemplateSerializer
    queryset = SourceFormTemplate.objects.all()

class SourceFormTemplateDetail(generics.RetrieveUpdateAPIView):
    serializer_class = SourceFormTemplateSerializer
    queryset = SourceFormTemplate.objects.all()
    lookup_field = "type"

class SourceList(generics.CreateAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()

    # TODO - handle unique constraint failure


class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
