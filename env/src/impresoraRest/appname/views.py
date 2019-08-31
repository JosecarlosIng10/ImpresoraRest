from django.shortcuts import render
from rest_framework import viewsets as meviewsets
from impresoraRest.appname.serializers import ToolSerializer
from impresoraRest.appname.models import Tool

class ToolViewSet(meviewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer