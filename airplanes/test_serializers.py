
from django.test import TestCase
from airplanes.serializers import AeroplaneSerializer

class AirplaneSerializerTest(TestCase):
    def test_valid_data(self):
        data = {'id': 1, 'passenger_assumptions': 100}
        serializer = AeroplaneSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_id(self):
        data = {'id': 0, 'passenger_assumptions': 100}
        serializer = AeroplaneSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('id', serializer.errors)

    def test_invalid_passenger_assumptions(self):
        data = {'id': 1, 'passenger_assumptions': -10}
        serializer = AeroplaneSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('passenger_assumptions', serializer.errors)

    def test_read_only_fields(self):
        instance_data = {'id': 1, 'passenger_assumptions': 100}
        serializer = AeroplaneSerializer(data=instance_data)
        serializer.is_valid()
        instance = serializer.save()

        # Attempt to modify read-only fields
        update_data = {'fuel_consumption': 10.5, 'max_flying_minutes': 150.0}
        serializer = AeroplaneSerializer(instance, data=update_data, partial=True)
        self.assertFalse(serializer.is_valid())

        # Check that read-only fields remain unchanged
        self.assertNotIn('fuel_consumption', serializer.validated_data)
        self.assertNotIn('max_flying_minutes', serializer.validated_data)
        

   

    def test_representation_customization(self):
        instance_data = {'id': 1, 'passenger_assumptions': 100}
        serializer = AeroplaneSerializer(data=instance_data)
        serializer.is_valid()
        instance = serializer.save()

        # Check the serialized representation
        serialized_data = serializer.data
        self.assertIn('custom_field', serialized_data)
        
