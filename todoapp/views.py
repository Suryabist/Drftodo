

# Create your views here.
from rest_framework import viewsets

from todoapp.serializers import TodoSerialziers
from .models import todo


class todoview(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerialziers



