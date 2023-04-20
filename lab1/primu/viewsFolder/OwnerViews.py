from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from primu.models import Owners
from primu.serializers import OwnersSerializer
from rest_framework.response import Response
from rest_framework import status


class OwnersApiView(APIView):
    @extend_schema(responses={200: OwnersSerializer(many=True)})
    def get(self, request):
        owners = Owners.objects.all()
        serializer = OwnersSerializer(owners, many=True)
        return Response(serializer.data)

    @extend_schema(request=OwnersSerializer, responses={201: OwnersSerializer})
    def post(self, request):
        serializer = OwnersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class OwnersDetailView(APIView):
    @extend_schema(responses={200: OwnersSerializer})
    def get(self, request, id):
        try:
            owner = Owners.objects.get(pk=id)
        except Owners.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OwnersSerializer(owner)
        return Response(serializer.data)

    @extend_schema(request=OwnersSerializer, responses={200: OwnersSerializer})
    def put(self, request, id):
        try:
            owner = Owners.objects.get(pk=id)
        except Owners.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OwnersSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={204: 'No Content'})
    def delete(self, request, id):
        try:
            owner = Owners.objects.get(pk=id)
        except Owners.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)