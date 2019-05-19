from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippet, or create a new snippet.
    """
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		

@api_view(['PUT', 'GET', 'DELETE'])		
def snippet_detail(request, pk, format=None):
	"""
	Retrive, update, delete a code snippet
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=404)
	
	
	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)
		
	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return	Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
