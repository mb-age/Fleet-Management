from django.db import models


class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=20, unique=True)  # Vehicle Identification Number
    registration_number = models.CharField(max_length=20)
    assigned_driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.license_number})"


class Route(models.Model):
    name = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    date_assigned = models.DateTimeField(auto_now_add=True)
    distance_km = models.DecimalField(max_digits=5, decimal_places=1)
    estimated_time_hours = models.DecimalField(max_digits=4, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.start_location} to {self.end_location}"


class VehicleStatus(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    fuel_level = models.CharField(max_length=10)
    brake_condition = models.CharField(max_length=10)
    tire_condition = models.CharField(max_length=10)
    last_service_date = models.DateField()

    def __str__(self):
        return f"Status of {self.vehicle.vin}"
