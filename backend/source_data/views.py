from django.http import JsonResponse
from rest_framework import generics
from source_data.serializers import SourceFormTemplateSerializer, SourceSerializer
from source_data.models import SourceFormTemplate, Source
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_source_types(request):
    source_types = dict(SourceFormTemplate.SourceType.choices)

    return JsonResponse(source_types)

class SourceFormTemplateList(generics.CreateAPIView):
    serializer_class = SourceFormTemplateSerializer
    queryset = SourceFormTemplate.objects.all()

class SourceFormTemplateDetail(generics.RetrieveUpdateAPIView):
    serializer_class = SourceFormTemplateSerializer
    queryset = SourceFormTemplate.objects.all()
    lookup_field = "source_type"

class SourceList(generics.CreateAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()

    # TODO - handle unique constraint failure


class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
