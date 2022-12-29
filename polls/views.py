from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework import status
from rest_framework.response import Response

from polls.models import Bar
from polls.serializers import BarSerializer


class FooAPIView(GenericAPIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

class BarsAPIView(ListAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

