from django.db.models import Count
from rest_framework import serializers
from .models import Car, Rims, RaceTracks, Owners, OwnersCars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'mod', 'chasisNr', 'hp', 'yearOfRegistration']


class CarOwnerSerializer(serializers.ModelSerializer):
    num_cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Owners
        fields = ['id', 'name', 'num_cars']


class CarRimsSerializer(serializers.ModelSerializer):
    num_rims = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'mod', 'num_rims']


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = ['id', 'name', 'addres', 'cnp']


class OwnersCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnersCars
        fields = ['id', 'price', 'kmWhenBought', 'car', 'owner']


class RimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rims
        fields = ['id', 'rimBrand', 'rimModel', 'height', 'width', 'carModel']


class RaceTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceTracks
        fields = ['id', 'name', 'lenght', 'style', 'surface', 'recordHolder']


class CarSerializerdetail(serializers.ModelSerializer):
    rims = RimsSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'mod', 'rims']
        depth = 1


class RimsSerializerDetail(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Rims
        fields = '__all__'
        depth = 1
