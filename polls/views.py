import logging

from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
)
from rest_framework import status
from rest_framework.response import Response

from polls.models import Bar
from polls.serializers import BarSerializer

logger = logging.getLogger(__name__)


class FooAPIView(GenericAPIView):
    def get(self, request, format=None):

        return Response(status=status.HTTP_200_OK)


class BarsAPIView(ListAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["bor_value"] = None

        return context


class BarAPIView(GenericAPIView):
    def post(self, request, format=None):

        serializer = BarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            logger.debug(f"From view >> {Bar.objects.count()}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
