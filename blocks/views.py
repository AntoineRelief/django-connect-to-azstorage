from django.shortcuts import render

from blocks.serializers import BlockSerializer
from .models import Block
from rest_framework import viewsets

# Create your views here.
class BlockViewSet(viewsets.ModelViewSet):
  queryset = Block.objects.all()
  serializer_class = BlockSerializer