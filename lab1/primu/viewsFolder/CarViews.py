from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from primu.serializers import CarSerializer, CarRimsSerializer
from rest_framework.response import Response

from primu.models import Car
from rest_framework import status


class CarApiView(APIView):
    @extend_schema(responses={201: CarSerializer}, )
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    @extend_schema(request=CarSerializer, responses={201: CarSerializer})
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class CarDetailView(APIView):
    @extend_schema(responses={200: CarSerializer})
    def get(self, request, id):
        try:
            car = Car.objects.get(pk=id)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    @extend_schema(request=CarSerializer, responses={200: CarSerializer})
    def put(self, request, id):
        try:
            car = Car.objects.get(pk=id)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={204: "No Content"})
    def delete(self, request, id):
        try:
            car = Car.objects.get(pk=id)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarRimsReport1ApiView(APIView):
    @extend_schema(responses={200: CarRimsSerializer(many=True)})
    def get(self, request):
        cars = Car.objects.annotate(num_rims=Count('rims'))
        cars = cars.order_by('-num_rims')
        serializer = CarRimsSerializer(cars, many=True)
        return Response(serializer.data)
