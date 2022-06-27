import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


#
# class WomenModel:
#     def __init__(self, title, context):
#         self.title = title
#         self.context = context


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     context = serializers.CharField()

#
# def encode():
#     model = WomenModel('Angilina Djoli', 'context: Andjelina djoli')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Anjelina Jolie", "context":"Context: Anjelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     context = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.context = validated_data.get('context', instance.context)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance

class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = ('__all__')