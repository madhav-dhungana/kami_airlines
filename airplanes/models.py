from django.db import models

class Aeroplane(models.Model):
    # Unique identifier for the airplane
    id = models.IntegerField(primary_key=True)

    # Estimated number of passengers the airplane can carry
    passenger_assumptions = models.IntegerField()

    # Calculated fuel consumption per minute for the airplane
    fuel_consumption = models.FloatField(null=True, blank=True)

    # Maximum flying minutes based on fuel tank capacity and consumption
    max_flying_minutes = models.FloatField(null=True, blank=True)

    def __str__(self):
        # Display the airplane's id when converting to a string
        return str(self.id)

    class Meta:
        # Order airplanes by their id in ascending order
        ordering = ["id"]

        # Display the plural name for the model as "id" in the admin interface
        verbose_name_plural = "id"

        
        
