from django.http import Http404
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrive, update, delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
