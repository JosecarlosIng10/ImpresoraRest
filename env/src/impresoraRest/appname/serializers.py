from impresoraRest.appname.models import PrintController
from rest_framework import serializers
 
class ToolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrintController
        fields = '__all__'
    
