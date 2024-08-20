from django.test import TestCase

from ..models import Vehicle, Driver, Route, VehicleStatus


class VehicleModelTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Jan",
            last_name="Kowalski",
            license_number="XYZ123456",
            phone_number="123456789",
            address="ul. Nowa 5, Warszawa"
        )
        self.vehicle = Vehicle.objects.create(
            make="Toyota",
            model="Corolla",
            year=2018,
            vin="1HGCM82633A123456",
            registration_number="ABC1234",
            assigned_driver=self.driver
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.make, "Toyota")
        self.assertEqual(self.vehicle.model, "Corolla")
        self.assertEqual(self.vehicle.year, 2018)
        self.assertEqual(self.vehicle.vin, "1HGCM82633A123456")
        self.assertEqual(self.vehicle.registration_number, "ABC1234")
        self.assertEqual(self.vehicle.assigned_driver, self.driver)

    def test_driver_creation(self):
        self.assertEqual(self.driver.first_name, "Jan")
        self.assertEqual(self.driver.last_name, "Kowalski")
        self.assertEqual(self.driver.license_number, "XYZ123456")
        self.assertEqual(self.driver.phone_number, "123456789")


class RouteModelTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            first_name="Anna",
            last_name="Nowak",
            license_number="XYZ7891011",
            phone_number="987654321",
            address="ul. Stara 8, Kraków"
        )
        self.vehicle = Vehicle.objects.create(
            make="Ford",
            model="Fiesta",
            year=2017,
            vin="1HGCM82633A654321",
            registration_number="DEF5678",
            assigned_driver=self.driver
        )
        self.route = Route.objects.create(
            name="Route A",
            start_location="Warszawa",
            end_location="Kraków",
            vehicle=self.vehicle,
            driver=self.driver,
            distance_km=300.0,
            estimated_time_hours=3.5,
            start_time="2024-08-20 08:00:00"
        )

    def test_route_creation(self):
        self.assertEqual(self.route.name, "Route A")
        self.assertEqual(self.route.start_location, "Warszawa")
        self.assertEqual(self.route.end_location, "Kraków")
        self.assertEqual(self.route.vehicle, self.vehicle)
        self.assertEqual(self.route.driver, self.driver)
        self.assertEqual(self.route.distance_km, 300.0)
        self.assertEqual(self.route.estimated_time_hours, 3.5)


class VehicleStatusModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            make="Nissan",
            model="Micra",
            year=2016,
            vin="1HGCM82633A987654",
            registration_number="GHI7890",
        )
        self.vehicle_status = VehicleStatus.objects.create(
            vehicle=self.vehicle,
            fuel_level="100%",
            brake_condition="Good",
            tire_condition="New",
            last_service_date="2024-01-15"
        )

    def test_vehicle_status_creation(self):
        self.assertEqual(self.vehicle_status.vehicle, self.vehicle)
        self.assertEqual(self.vehicle_status.fuel_level, "100%")
        self.assertEqual(self.vehicle_status.brake_condition, "Good")
        self.assertEqual(self.vehicle_status.tire_condition, "New")
        self.assertEqual(self.vehicle_status.last_service_date, "2024-01-15")
