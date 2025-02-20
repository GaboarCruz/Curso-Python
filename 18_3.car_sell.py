class Car:
    def __init__(self, name, model, price, car_type):
        self.name = name
        self.model = model
        self.price = price
        self.car_type = car_type
        self.available = True
    
    def sell_car(self):
            self.available = False
            #print(f"El carro {self.name} ah sido vendido")

class Customer:
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido
        self.customer_cars = []

    def buy_car(self, car):
        if car.available:
            car.sell_car()
            self.customer_cars.append(car)
            print(f"El comprador: {self.name} {self.apellido} ha comprado el carro: {car.name} {car.model}")

class CarCollection:
    def __init__(self):
        self.cars = []
        self.customers = []
    
    def add_cars(self, car):
        self.cars.append(car)
       #print(f"Se ah añadido el carro: {car.name} {car.model}")

    def add_customer(self, customer):
        self.customers.append(customer)
        #print(f"Se ah añadido al cliente: {customer.name}")

    def show_cars(self):
        print("Los carros disponibles son:")
        for car in self.cars:
            if car.available:
                print(f"Nombre del carro: {car.name}\n\tModelo: {car.model}\n\tPrecio: {car.price}\n\tTipo: {car.car_type}")

car1 = Car("Toyota", "Agya", 12000, "Hatchback")
car2 = Car("Kia", "Soluto", 14000, "Sedán")
car3 = Car("Hyundai", "Grand i10", 13000, "Hatchback")
customer1 = Customer("Juan", "Pérez")
customer2 = Customer("María", "González")

coleccion = CarCollection()

coleccion.add_cars(car1)
coleccion.add_cars(car2)
coleccion.add_cars(car3)
coleccion.add_customer(customer1)
coleccion.add_customer(customer2)
coleccion.show_cars()
customer1.buy_car(car1)
customer2.buy_car(car2)
coleccion.show_cars()
