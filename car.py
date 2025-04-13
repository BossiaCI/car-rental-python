class Car:
    def __init__(self, id:int, brand: str, model:str):
        self.id = id
        self.brand = brand
        self.model = model
        self.available = True

    def is_available(self) -> bool:
        return self.available
    
    def mark_rented(self):
        self.available = False

    def mark_available(self):
        self.available = True
    
    def __str__(self):
        return f"Car[id={self.id}, brand={self.brand}, model={self.model}, available={self.available}]"

