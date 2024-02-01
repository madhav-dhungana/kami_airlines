
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Aeroplane
from .serializers import AeroplaneSerializer

class AeroplaneListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating Aeroplanes.

    Allows users to list all existing Aeroplanes and create new ones.
    Includes automatic calculation of fuel consumption and maximum flying minutes
    for newly created or updated Aeroplanes.

    Attributes:
    - queryset: Set of Aeroplanes to be used by the view.
    - serializer_class: Serializer class for Aeroplane objects.
    """

    queryset = Aeroplane.objects.all()
    serializer_class = AeroplaneSerializer

    def perform_create(self, serializer):
        """
        Perform additional actions after creating an Aeroplane.

        Calculates and updates fuel consumption and maximum flying minutes.
        """
        airplane = serializer.save()
        self.calculate_fuel_consumption(airplane)
        self.calculate_max_flying_minutes(airplane)

    def perform_update(self, serializer):
        """
        Perform additional actions after updating an Aeroplane.

        Calculates and updates fuel consumption and maximum flying minutes.
        """
        airplane = serializer.save()
        self.calculate_fuel_consumption(airplane)
        self.calculate_max_flying_minutes(airplane)

    def calculate_fuel_consumption(self, airplane):
        """
        Calculate and update fuel consumption for an Aeroplane.

        Formula: fuel_consumption = (0.80 * airplane.id) + (0.002 * airplane.passenger_assumptions)
        """
        fuel_consumption = (0.80 * airplane.id) + (0.002 * airplane.passenger_assumptions)
        airplane.fuel_consumption = fuel_consumption
        airplane.save()

    def calculate_max_flying_minutes(self, airplane):
        """
        Calculate and update maximum flying minutes for an Aeroplane.

        Formula: max_flying_minutes = fuel_tank_capacity / airplane.fuel_consumption
        """
        fuel_tank_capacity = 200 * airplane.id
        max_flying_minutes = fuel_tank_capacity / airplane.fuel_consumption
        airplane.max_flying_minutes = max_flying_minutes
        airplane.save()

    def list(self, request, *args, **kwargs):
        """
        List all Aeroplanes.

        Returns a response with serialized Aeroplanes and HTTP status 200.
        """
        airplanes = Aeroplane.objects.all()
        serializer = self.get_serializer(airplanes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AeroplaneDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific Aeroplane.

    Allows users to retrieve details, update, or delete a specific Aeroplane.

    Attributes:
    - queryset: Set of Aeroplanes to be used by the view.
    - serializer_class: Serializer class for Aeroplane objects.
    """

    queryset = Aeroplane.objects.all()
    serializer_class = AeroplaneSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of a specific Aeroplane.

        Returns a response with serialized Aeroplane and HTTP status 200.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
