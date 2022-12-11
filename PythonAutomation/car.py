class Car():

    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def get_car_info(self):
        car_info = "Model of the car is " + self.model + ", it was produced in " + str(self.year) + " year " + "with the " + str(self.engine) + " capacity, " + "its price is " + str(self.price) + " and its mileage is " + str(self.mileage)
        return car_info
audi = Car('Q7', 2021, 8, 120000, 5)

print(audi.get_car_info())
