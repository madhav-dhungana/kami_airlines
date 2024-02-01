
from rest_framework import serializers
from .models import Aeroplane

class AeroplaneSerializer(serializers.ModelSerializer):
    """
    Serializer for the Aeroplane model.

    Serializes and validates data for the Aeroplane model, including custom validations
    for the 'id' and 'passenger_assumptions' fields. Also includes a custom representation
    to add an additional 'custom_field' in the serialized output.

    Attributes:
    - id: Unique identifier for the airplane.
    - passenger_assumptions: Estimated number of passengers the airplane can carry.
    - fuel_consumption: Calculated fuel consumption per minute for the airplane.
    - max_flying_minutes: Maximum flying minutes based on fuel tank capacity and consumption.
    """

    class Meta:
        # Specify the Aeroplane model and fields to include in the serializer
        model = Aeroplane
        fields = ['id', 'passenger_assumptions', 'fuel_consumption', 'max_flying_minutes']

        # Specify read-only fields in the serializer
        read_only_fields = ['fuel_consumption', 'max_flying_minutes']

    def validate_id(self, value):
        """
        Validate that the 'id' field is a positive integer.
        """
        if value <= 0:
            raise serializers.ValidationError("Airplane ID must be a positive integer.")
        return value

    def validate_passenger_assumptions(self, value):
        """
        Validate that 'passenger_assumptions' is a non-negative integer.
        """
        if value < 0:
            raise serializers.ValidationError("Passenger assumptions must be a non-negative integer.")
        return value

    def validate(self, data):
        """
        Validate the entire data dictionary, checking for invalid values in 'id' and 'passenger_assumptions'.
        """
        id_value = data.get('id', 0)
        assumptions_value = data.get('passenger_assumptions', 0)

        if id_value <= 0 or assumptions_value < 0:
            raise serializers.ValidationError("Invalid values for Airplane ID or Passenger Assumptions.")

        return data

    def to_representation(self, instance):
        """
        Customize the serialized representation by adding a 'custom_field'.
        """
        representation = super().to_representation(instance)
        representation['custom_field'] = 'custom_value'
        return representation
