from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema

from .models import Car, Rims, RaceTracks, Owners, OwnersCars
from .serializers import CarSerializer, RimsSerializer, RaceTracksSerializer, CarSerializerdetail, RimsSerializerDetail, \
    OwnersSerializer, OwnersCarsSerializer, CarOwnerSerializer, CarRimsSerializer
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView


class RimsFilter(filters.FilterSet):
    class Meta:
        model = Rims
        fields = {
            'rimBrand': ['icontains'],
            'height': ['gte']
        }

"""
class CarApiView(GenericAPIView):
    @extend_schema(responses={201: CarSerializer}, )
    @api_view(['GET', 'POST'])
    def cars_list(request):
        if request.method == 'GET':
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
                """
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



class MultipleRimsCarView(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def bulkAdd(request):
        rim_id_new_brand_list = request.data.get('rims_id_new_brand_list')

        # Loop through the list of car ids and new car brands to update
        for item in rim_id_new_brand_list:
            rim = Rims.objects.get(id=item['rims_id'])
            rim.carModel = Car.objects.get(id=item['newcar'])
            rim.save()

        return Response({'message': 'Cars updated successfully.'})


@api_view(['GET', 'POST'])
def owners_list(request):
    serializer_class = OwnersSerializer
    if request.method == 'GET':
        cars = Owners.objects.all()
        serializer = OwnersSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OwnersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def ownersCars_list(request):
    serializer_class = OwnersCarsSerializer
    if request.method == 'GET':
        cars = OwnersCars.objects.all()
        serializer = OwnersCarsSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OwnersCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def rims_list(request):
    serializer_class = RimsSerializer
    id = request.query_params.get('id')
    height1 = request.query_params.get('height')
    if request.method == 'GET':
        if id:
            rims = Rims.objects.filter(id=id)
        elif height1:
            rims = Rims.objects.filter(height__gt=height1)
        else:
            rims = Rims.objects.all()
        serializer = RimsSerializer(rims, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RimsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
def racetracks_list(request):
    serializer_class = RaceTracksSerializer
    if request.method == 'GET':
        cars = RaceTracks.objects.all()
        serializer = RaceTracksSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RaceTracksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, id):
    # serializer_class = CarSerializer
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializerdetail(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def owners_detail(request, id):
    serializer_class = OwnersSerializer
    try:
        car = Owners.objects.get(pk=id)
    except Owners.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OwnersSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OwnersSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def ownersCars_detail(request, id):
    serializer_class = OwnersCarsSerializer
    try:
        car = OwnersCars.objects.get(pk=id)
    except OwnersCars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OwnersCarsSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OwnersCarsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def rims_detail(request, id):
    # serializer_class = RimsSerializer
    try:
        car = Rims.objects.get(pk=id)
    except Rims.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RimsSerializerDetail(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RimsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def racetracks_detail(request, id):
    serializer_class = RaceTracksSerializer
    try:
        car = RaceTracks.objects.get(pk=id)
    except RaceTracks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RaceTracksSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RaceTracksSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def car_owner_report(request):
    owners = Owners.objects.annotate(num_cars=Count('ownerscars'))

    owners = owners.order_by('-num_cars')

    context = {'owners': owners}
    return render(request, 'owner_report.html', context)


def car_rims_report(request):
    cars = Car.objects.annotate(num_cars=Count('rims'))
    cars = cars.order_by('-num_cars')
    context = {'cars': cars}
    return render(request, 'car_report.html', context)


@api_view(['GET', 'POST'])
def car_owner_report1(request):
    serializer_class = CarOwnerSerializer
    if request.method == 'GET':
        owners = Owners.objects.annotate(num_cars=Count('ownerscars'))
        owners = owners.order_by('-num_cars')
        serializer = CarOwnerSerializer(owners, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def car_rims_report1(request):
    serializer_class = CarRimsSerializer
    if request.method == 'GET':
        cars = Car.objects.annotate(num_rims=Count('rims'))
        cars = cars.order_by('-num_rims')
        serializer = CarRimsSerializer(cars, many=True)
        return Response(serializer.data)
