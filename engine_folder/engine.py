
class Engine:
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
    def needs_service(self):
        pass