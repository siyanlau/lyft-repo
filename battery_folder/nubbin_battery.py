from datetime import date
from .battery import Battery 


class NubbinBattery(Battery):
    def needs_service(self):
        current_date = date.today()
        if ((current_date - self.last_service_date).days >= 365 * 4):
            return True
        else:
            return False

# last_date = date(2019, 8, 26)
# my_battery = NubbinBattery(last_date)
# # print(my_battery.needs_service())