from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# GET, POST 가능
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# GET, POST, UPDATE, DELETE 가능
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
