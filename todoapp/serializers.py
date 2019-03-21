from rest_framework import serializers
from .models import todo

class TodoSerialziers(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('__all__')


class TodominiSerialziers(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('id', 'title')




