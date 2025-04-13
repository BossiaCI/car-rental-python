from datetime import date
from car import Car
from customer import Customer
from payment_processor import PaymentProcessor
from reservation import Reservation


class RentalService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.cars = []
        self.customers = []
        self.reservations = []
        self.payment_processor = payment_processor
        self.reservation_counter = 1

    def add_car(self, car: Car):
        self.cars.append(car)

    def register_customer(self, customer: Customer):
        self.customers.append(customer)

    def create_reservation(self, customer_id: int, car_id: int, start_date: date, end_date: date) -> Reservation:
        customer = next((c for c in self.customers if c.id == customer_id), None)
        car = next((c for c in self.cars if c.id == car_id), None)
        if customer is None or car is None or not car.is_available():
            print("Reservation failed: invalid customer or car unavailable")
            return None

        reservation = Reservation(self.reservation_counter, customer, car, start_date, end_date)
        if self.payment_processor.process_payment(reservation.total_cost):
            car.mark_rented()
            self.reservations.append(reservation)
            self.reservation_counter += 1
            print("Reservation created:", reservation)
            return reservation
        else:
            print("Payment failed. Reservation not created.")
            return None

    def return_car(self, reservation_id: int) -> bool:
        reservation = next((r for r in self.reservations if r.id == reservation_id), None)
        if reservation:
            reservation.car.mark_available()
            print(f"Car returned for reservation: {reservation_id}")
            return True
        else:
            print(f"Reservation not found for id: {reservation_id}")
            return False

    def print_status(self):
        print("Cars in fleet:")
        for car in self.cars:
            print(car)
        print("Registered customers:")
        for customer in self.customers:
            print(customer)
        print("Reservations made:")
        for reservation in self.reservations:
            print(reservation)
