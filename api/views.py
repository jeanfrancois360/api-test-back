from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member
from .serializers import MemberSerializer

@api_view(['GET'])
def getMembers(request):
    Members = Member.objects.all()
    serializer = MemberSerializer(Members, many=True)
    return Response(serializer.data);

@api_view(['GET'])
def getMember(request, pk):
    Member = Member.objects.get(id=pk)
    serializer = MemberSerializer(Member, many=False)
    return Response(serializer.data);

@api_view(['POST'])
def addMember(request):
    serializer = MemberSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateMember(request, pk):
    Member = Member.objects.get(id=pk)
    serializer = MemberSerializer(Member, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMember(request, pk):
    Member = Member.objects.get(id=pk)
    Member.delete()
    return Response("Member was deleted")