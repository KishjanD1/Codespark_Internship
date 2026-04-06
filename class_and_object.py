import keyboard
import time

class bus: #createing class
    def __init__(self,b_number,b_color): #attributes of the bus
        self.b_number = b_number
        self.b_color = b_color


    def honk(self): #honk method created
        print(f"  A car with0  {self.b_number} number with {self.b_color} color honk in non-honk zone")

bus_details=bus(b_number=15648,b_color="red") #creating instance/objects

bus_details.honk() #using honk method with objects



