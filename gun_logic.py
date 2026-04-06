


import time
import keyboard

class gun:
    def __init__(self,g_model,g_ammo):
        self.g_model = g_model
        self.g_ammo = g_ammo
        self.g_max = self.g_ammo

    def fire(self):
        if self.g_ammo > 0 :
            print(f"{self.g_model} fire ammo {self.g_ammo} bang 3 bullet fired  - - - ")
            self.g_ammo -=3
            print(f"ammo left {self.g_ammo}")
        else :
            model.reload(self)

    def reload(self):
        self.g_ammo = self.g_max
        print(f"reloading.... {self.g_ammo} ammo loaded")



gun_type = "ak47"
ammo = 30
model = gun(g_model=gun_type,g_ammo=ammo)

print("press space to fire | R to reload")

while True:
    if keyboard.is_pressed("space"):
         model.fire()
         time.sleep(1)
    if keyboard.is_pressed("R"):
         model.reload()
         time.sleep(1)
    if keyboard.is_pressed("Q"):
        print("quit")
        break