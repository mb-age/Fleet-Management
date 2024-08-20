from flasgger import Swagger
from flask import Flask, jsonify, request
from flask_caching import Cache
from django_setup import *
from fleet.models import VehicleStatus, Vehicle


app = Flask(__name__)
swagger = Swagger(app)

# Cache config
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache retention time in seconds

cache = Cache(app)

# Mockup data on the technical condition of the vehicle
vehicle_status_data = {
    '1234ABC': {
        'fuel_level': '75%',
        'brake_condition': 'Good',
        'tire_condition': 'New',
        'last_service_date': '2024-05-01'
    },
    '5678XYZ': {
        'fuel_level': '50%',
        'brake_condition': 'Fair',
        'tire_condition': 'Worn',
        'last_service_date': '2024-03-15'
    },
}


@app.route('/vehicle_status/', methods=['GET'])
@cache.cached(timeout=300, key_prefix='vehicle_status')
def vehicle_status():
    vin = request.args.get('vin')
    if vin in vehicle_status_data:
        status_data = vehicle_status_data[vin]

        # Save or update VehicleStatus
        vehicle = Vehicle.objects.filter(vin=vin).first()
        if vehicle:
            VehicleStatus.objects.update_or_create(
                vehicle=vehicle,
                defaults={
                    'fuel_level': status_data['fuel_level'],
                    'brake_condition': status_data['brake_condition'],
                    'tire_condition': status_data['tire_condition'],
                    'last_service_date': status_data['last_service_date']
                }
            )
        return jsonify(status_data)
    else:
        return jsonify({'error': 'Vehicle not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
