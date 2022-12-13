class Car:
    def __init__(self, car_name, car_model, car_gas):
        self.car_name = car_name
        self.car_model = car_model
        self.car_gas = car_gas
        def __str__(self):
            return f"Car: {self.car_name}, {self.car_model}, {self.car_gas}"

class Driver(Car):
    def __init__(self, car, driver_name, driver_lastname, driver_age):
        super().__init__(car.car_name, car.car_model, car.car_gas)
        self.driver_name = driver_name
        self.driver_lastname = driver_lastname
        self.driver_age = driver_age
    
    def __str__(self):
        return f"Car: {self.car_name}, {self.car_model}, {self.car_gas}; Driver: {self.driver_name}, {self.driver_lastname}, {self.driver_age}"

class Coach(Car):
    def __init__(self, car, name, experience):
        super().__init__(car.car_name, car.car_model, car.car_gas)
        self.name = name
        self.experience = experience
    
    def __str__(self):
        return f"Coach: {self.name}, {self.experience}"
    
car = Car("Мерджам", "Катафалка", "Олио")
driver = Driver(car, "Пенчо", "Пенчев", 10)
print(driver)
coach = Coach(car, "Gospodin", 20)
print(coach)
