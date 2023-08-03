from .battery import Battery
from datetime import date

class SpindlerBattery(Battery):
    def needs_service(self):
        current_date = date.today()
        if ((current_date - self.last_service_date).days >= 365 * 2):
            return True
        else:
            return False

# last_date = date(2021, 7, 26)
# my_battery = SpindlerBattery(last_date)
# print(my_battery.needs_service())