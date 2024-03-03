from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from .models import BookModels



# create
@api_view(['POST'])
def postbook(request):
    books = BookModels.objects.all()
    serializer = BookSerializer(data = request.data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


# Reading
@api_view(['GET'])
def booklist(request):
    books = BookModels.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# update
@api_view(['POST'])
def updatebook(request,id):
    book = BookModels.objects.get(id=id)
    serializer = BookSerializer(instance = book ,data = request.data)
    if (serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)



# delete
@api_view(['DELETE'])
def deletebook(request,id):
    book = BookModels.objects.get(id=id)
    temp = book.name
    book.delete()
    return Response(f"{temp} has been deleted sucessfully.. please check now....!")