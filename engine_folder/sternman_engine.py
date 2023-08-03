# from abc import ABC
# from car import Car
from .engine import Engine
# from datetime import date

class SternmanEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, last_service_date, warning_light_is_on):
        Engine.__init__(self, last_service_mileage, current_mileage, last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on

# myEngine = SternmanEngine(10100, 20000, date.today(), False)
# print(myEngine.needs_service())