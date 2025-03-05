class Car:
    @staticmethod
    def start():
        print("car started")

    def stop(self):
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        


car1 = ToyotaCar("henry")
car2 = ToyotaCar("Hero")

print(car1.name)
car1.start()
car1.stop()
