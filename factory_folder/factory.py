
from datetime import datetime
from datetime import date
from ..car_folder import Car
from ..engine_folder import * #the __init__ file contains only the needed engine classes
from ..battery_folder import * #the __init__ file contains only the needed battery classes

current_date = date.today()

class Factory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)