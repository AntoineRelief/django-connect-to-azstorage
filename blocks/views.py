from django.shortcuts import render
from blocks.serializers import BlockSerializer
from .models import Block
from rest_framework import viewsets, generics, mixins, response
from .datalakeconnect import retrieve_file
import json

# Create your views here.
class BlockViewSet(viewsets.ModelViewSet):
  queryset = Block.objects.all()
  serializer_class = BlockSerializer

class DataLakeBlockDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Block.objects.all()
  serializer_class = BlockSerializer

  def get(self, request, *args, **kwargs):
    content = json.loads(retrieve_file(self.kwargs['pk']))
    serializer = self.get_serializer(data=content)
    serializer.is_valid()
    return response.Response(serializer.data)
    return self.retrieve(request, *args, **kwargs)