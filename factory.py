
from datetime import datetime
from datetime import date
from .car import Car
from .engine_folder import *
from .battery_folder import *

current_date = date.today()

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = sternman_engine.SternmanEngine(last_service_date, current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date)
        return Car(engine, battery)
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date)
        return Car(engine, battery)