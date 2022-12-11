class Car():

    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def get_car_info(self):
        car_info = "Model of the car is " + self.model + ", it was produced in " + str(self.year) + " year " + "with the " + str(self.engine) + " capacity, " + "its price is " + str(self.price) + " and its mileage is " + str(self.mileage) + " and it has " + str(self.wheels) + " wheels"
        return car_info

class Truck(Car):

    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.wheels = 8

    def get_truck_info(self):
        truck_info = f"Truck Info - Model: {self.model}, Year: {str(self.year)} Capacity: {str(self.engine)} Price:  {str(self.price)}, Mileage: {str(self.mileage)}, Wheels: {str(self.wheels)}"
        return truck_info


audi = Car('Q7', 2021, 8, 120000, 5)

print(audi.get_car_info())

lorry = Truck('Mercedes', 2020, 12, 145000, 10)
print(lorry.get_truck_info())

