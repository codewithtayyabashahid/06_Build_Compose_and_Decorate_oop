
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started."


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  

    def start_car(self):
        
        return f"{self.model} is starting... {self.engine.start()}"


# usage
engine1 = Engine(150)
my_car = Car("Toyota Corolla", engine1)

print(my_car.start_car())
