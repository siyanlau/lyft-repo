from battery.generic_battery import Battery
from datetime import date
import sys
sys.path.append("battery")

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    def needs_service(self):
        current_date = date.today()
        if ((current_date - self.last_service_date).days >= 365 * 2):
            return True
        else:
            return False

last_date = date(2019, 7, 26)
my_battery = SpindlerBattery(last_date)
print(my_battery.needs_service())