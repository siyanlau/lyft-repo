# from abc import ABC
# from car import Car
from .engine import Engine
from datetime import date

class CapuletEngine(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

# myEngine = CapuletEngine(10000, 20000, date.today())
# print(myEngine.needs_service())

