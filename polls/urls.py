from django.urls import path, re_path

from django.contrib import admin
from django.urls import include, path

from polls.views import BarAPIView, BarsAPIView, FooAPIView

urlpatterns = [
    path("foo/", FooAPIView.as_view()),
    path("bars/", BarsAPIView.as_view()),
    path("bar/", BarAPIView.as_view()),
]
