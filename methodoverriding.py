class Vehicle:
    def start(self):
        print("Starting vehicle")
        
class Car(Vehicle):
    def start(self):
        print("Starting car engine")
        
v = Vehicle()
c = Car()
v.start()  # Output: Starting vehicle
c.start()  # Output: Starting car engine
