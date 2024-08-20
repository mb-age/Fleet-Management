import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../fleet_manager')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fleet_manager.settings')
django.setup()

