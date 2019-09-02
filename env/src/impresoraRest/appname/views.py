from django.shortcuts import render
from rest_framework import viewsets as meviewsets
from impresoraRest.appname.serializers import ToolSerializer
from impresoraRest.appname.models import PrintController

class ToolViewSet(meviewsets.ModelViewSet):
    queryset = PrintController.objects.all()
    serializer_class = ToolSerializer