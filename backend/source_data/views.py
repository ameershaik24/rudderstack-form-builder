from rest_framework import generics
from source_data.serializers import SourceFormTemplateSerializer, SourceSerializer
from source_data.models import SourceFormTemplate, Source

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
