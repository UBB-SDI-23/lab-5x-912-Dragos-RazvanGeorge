from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from primu.models import OwnersCars, Owners
from primu.serializers import OwnersCarsSerializer, CarOwnerSerializer


class OwnersCarsApiView(APIView):
    @extend_schema(responses={200: OwnersCarsSerializer(many=True)}, )
    def get(self, request):
        cars = OwnersCars.objects.all()
        serializer = OwnersCarsSerializer(cars, many=True)
        return Response(serializer.data)

    @extend_schema(request=OwnersCarsSerializer, responses={201: OwnersCarsSerializer()})
    def post(self, request):
        serializer = OwnersCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class OwnersCarsDetailApiView(APIView):
    @extend_schema(responses={200: OwnersCarsSerializer})
    def get(self, request, id):
        try:
            car = OwnersCars.objects.get(pk=id)
        except OwnersCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OwnersCarsSerializer(car)
        return Response(serializer.data)

    @extend_schema(request=OwnersCarsSerializer, responses={200: OwnersCarsSerializer})
    def put(self, request, id):
        try:
            car = OwnersCars.objects.get(pk=id)
        except OwnersCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OwnersCarsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={204: 'No Content'})
    def delete(self, request, id):
        try:
            car = OwnersCars.objects.get(pk=id)
        except OwnersCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarOwnerReport1ApiView(APIView):
    @extend_schema(responses={200: CarOwnerSerializer(many=True)})
    def get(self, request):
        owners = Owners.objects.annotate(num_cars=Count('ownerscars')).order_by('-num_cars')
        serializer = CarOwnerSerializer(owners, many=True)
        return Response(serializer.data)
