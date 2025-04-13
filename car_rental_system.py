from datetime import date, timedelta
from car import Car
from credit_card_payment import CreditCardPayment
from customer import Customer
from rental_service import RentalService


if __name__ == "__main__":
    # Create payment processor instance
    payment_processor = CreditCardPayment("1234-5678-9012-3456", 123, date(2026, 12, 31))
    
    # Initialize rental service with dependency injection
    rental_service = RentalService(payment_processor)
    
    # Add cars to fleet
    rental_service.add_car(Car(1, "Toyota", "Camry"))
    rental_service.add_car(Car(2, "Honda", "Accord"))
    
    # Register customers
    rental_service.register_customer(Customer(1, "Alice", "A1234567"))
    rental_service.register_customer(Customer(2, "Bob", "B7654321"))
    
    # Create a reservation
    res1 = rental_service.create_reservation(1, 1, date.today(), date.today() + timedelta(days=3))
    # Attempt a reservation with same car which should fail
    res2 = rental_service.create_reservation(2, 1, date.today(), date.today() + timedelta(days=2))
    
    # Return the car for the first reservation
    if res1:
        rental_service.return_car(res1.id)
    
    # Print current system status
    rental_service.print_status()