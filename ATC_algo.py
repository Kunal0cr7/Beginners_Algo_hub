import random
import time

class Aircraft:
    def __init__(self, callsign):
        self.callsign = callsign
        self.altitude = 0
        self.speed = 0

    def climb(self):
        self.altitude += random.randint(1000, 3000)
        print(f"{self.callsign} is climbing to {self.altitude} feet.")

    def descend(self):
        self.altitude -= random.randint(1000, 3000)
        if self.altitude < 0:
            self.altitude = 0
        print(f"{self.callsign} is descending to {self.altitude} feet.")

    def accelerate(self):
        self.speed += random.randint(10, 30)
        print(f"{self.callsign} is accelerating to {self.speed} knots.")

    def decelerate(self):
        self.speed -= random.randint(10, 30)
        if self.speed < 0:
            self.speed = 0
        print(f"{self.callsign} is decelerating to {self.speed} knots.")

def main():
    aircraft_list = [Aircraft("Flight123"), Aircraft("Flight456"), Aircraft("Flight789")]

    while True:
        for aircraft in aircraft_list:
            action = random.choice(["climb", "descend", "accelerate", "decelerate"])
            if action == "climb":
                aircraft.climb()
            elif action == "descend":
                aircraft.descend()
            elif action == "accelerate":
                aircraft.accelerate()
            elif action == "decelerate":
                aircraft.decelerate()

        print("\nWaiting for updates...\n")
        time.sleep(5)

if __name__ == "__main__":
    main()
