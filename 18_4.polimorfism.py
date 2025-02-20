class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")
    
    #Abstracción
    def check_available(self):
        return self.is_available
    
    #Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
    
    #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No esta disponible"

#Herencia
class Bike(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"

     #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No esta disponible"

#Herencia
class Truck(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} esta en marcha"
        else:
            return f"El camión {self.brand} no esta disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No esta disponible"
        

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchase_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available:
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ah sido añadido al inventario")

    def add_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El {customer.name} ah sido añadido")

    def show_available_vehicles(self):
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"-{vehicle.brand} por {vehicle.get_price()}")


car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Muestra todos los vehiculos
dealership.show_available_vehicles()

# Ve disponibilidad del carro
customer1.inquire_vehicle(car1)

# Compra el carro
customer1.buy_vehicle(car1)
