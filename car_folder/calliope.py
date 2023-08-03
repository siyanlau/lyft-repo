from datetime import datetime
from .car import Car
from ..engine_folder.capulet_engine import CapuletEngine
from ..battery_folder.spindler_battery import SpindlerBattery


# class Calliope(Car):
#     def __init__(self, CapuletEngine, SpinderBattery):
#         super().__init__(engine, battery)
#     def needs_service(self):
#         pass
        # service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        # if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
        #     return True
        # else:
        #     return False
