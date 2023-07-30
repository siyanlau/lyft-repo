from datetime import datetime

class NubbinBattery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    def needs_service(self):
        current_date = 