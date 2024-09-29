

import datetime

#Insert your classes here
class CarModel:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Brand: {self.brand} Model: {self.model}"
    
class Service:
    def __init__(self, date, operation, price):
        self.date = date
        self.operation = operation
        self.price = price

    def __str__(self):
        return f"\tDate: {self.date.strftime('%d.%m.%Y')} Operation: {self.operation} Price: {self.price}"
    
class Car:
    def __init__(self, name, model, bought, price, boughtplace):
        self.name = name
        self.model = model
        self.bought = bought
        self.price = price
        self.boughtplace = boughtplace
        self.services = []

    def addService(self, service):
        self.services.append(service)

    def __str__(self):
        service_history = "\n".join([str(service) for service in self.services])
        return f"Name:  {self.name}\n{self.model}\nBought: {self.bought.strftime('%d.%m.%Y')}\nService history: \n{service_history}\nBought place:  {self.boughtplace}\n"
    
class CarStorage:
    def __init__(self):
        self.cars = []

    def addCar(self, car):
        self.cars.append(car)

    def print(self):
        print("The list of my sweet cars:\n")
        for car in self.cars:
            print(car)
if __name__ == '__main__':
    #Main program, dont modify!
    myCarStorage = CarStorage()

    volvo_v70 = CarModel("Volvo", "V70")
    porsche_cyaenne = CarModel("Porsche", "Cayanne")
    datsun_100a = CarModel("Datsun", "100A")

    car1 = Car(name="Old faithful",model=volvo_v70,
               bought=datetime.datetime(2020, 1,1),price= 1200, boughtplace="Don't remember")
    service1 = Service(date = datetime.datetime(2021,1,11),operation="New tyres", price= 300 )
    service2 = Service(date = datetime.datetime(2019, 3,4),operation="Oils changed", price = 234 )
    car1.addService(service1)
    car1.addService(service2)
    myCarStorage.addCar(car1)

    car2 = Car(name="Porky",model=porsche_cyaenne,
               bought=datetime.datetime(2021, 1,13),price= 11200, boughtplace="Porche Center, Helsinki")
    service1 = Service(date = datetime.datetime(2021,3,11),operation="New tyres", price= 1300 )
    service2 = Service(date = datetime.datetime(2019, 12,4),operation="Exhaust pipe changed", price = 2324 )
    car2.addService(service1)
    car2.addService(service2)
    myCarStorage.addCar(car2)

    car3 = Car(name="A",model=datsun_100a,
               bought=datetime.datetime(1991, 11,13),price= 200, boughtplace="Auli Autoilija, Pori")
    service1 = Service(date = datetime.datetime(1992,3,11),operation="New tyres", price= 400 )
    service2 = Service(date = datetime.datetime(1995,5,2),operation="New tyres", price= 440 )
    service3 = Service(date = datetime.datetime(2001, 12,4),operation="Timing belt replaced", price = 500 )
    service4 = Service(date = datetime.datetime(2019, 12,4),operation="Exhaust pipe repaired", price = 324 )
    car3.addService(service1)
    car3.addService(service2)
    car3.addService(service3)
    car3.addService(service4)
    myCarStorage.addCar(car3)

    #Print all cars with information
    myCarStorage.print()
