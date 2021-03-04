from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializers import UserssSerializer
from .models import Userss 


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/userss-list/',
        'Detail View': '/userss-detail/<str:pk>/',
        'Create': '/userss-create/',
        'Update': '/userss-update/<str:pk>/',
        'Delete': '/userss-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def UserssList(request):
    usersss = Userss.objects.all().order_by('-id')
    serializer = UserssSerializer(usersss, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def UserssDetail(request,pk):
    users = Userss.objects.get(id=pk)
    serializer = UserssSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserssCreate(request):
    serializer = UserssSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def UserssUpdate(request, pk):
    users = Userss.objects.get(id=pk)
    serializer = UserssSerializer(instance = users, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def UserssDelete(request, pk):
    users = Userss.objects.get(id=pk)
    users.delete()
    return Response("Item succesfully Deleted")

