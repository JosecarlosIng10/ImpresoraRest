from rest_framework  import serializers
from impresoraRest.appname.models import Tool
 
class ToolSerializer(serializers.Serializer):
    class Meta:
        model = Tool
        fields = '__all__'
    
    def create(self, validated_data):
        return Tool.objects.create(**validated_data)