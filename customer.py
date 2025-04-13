class Customer:
    def __init__(self, id:int, name:str, license_number: str):
        self.id = id
        self.name = name
        self.license_number = license_number
    
    def __str__(self):
        return f"Customer[id={self.id}, name={self.name}, license={self.license_number}]"