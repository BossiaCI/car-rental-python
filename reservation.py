from datetime import date
from car import Car
from customer import Customer


class Reservation:
    DAILY_RATE = 50.0

    def __init__(self, id: int, customer: Customer, car: Car, start_date: date, end_date: date):
        self.id = id
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self) -> float:
        days = (self.end_date - self.start_date).days
        if days == 0:
            days = 1  # Minimum one day charge
        return days * self.DAILY_RATE

    def __str__(self):
        return (f"Reservation[id={self.id}, customer={self.customer}, car={self.car}, "
                f"from={self.start_date}, to={self.end_date}, cost={self.total_cost}]")