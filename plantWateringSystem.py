import random
import time


class WateringController:
    def __init__(self, mositureLevel):
        self.moistureLevel = mositureLevel

    def senseMoisture(self):
        return self.moistureLevel.get_moisture_level()

    def decideAction(self):
        moistureLevel = self.senseMoisture()

        if moistureLevel < 40:
            return "Water the plants"
        else:
            return "sit idle"





class MoistureSensor:
    def __init__(self, moistureLevel):
        self.moistureLevel = moistureLevel

    def get_moisture_level(self):
        return self.moistureLevel




def moisture_level():
    while True:
        # Simulate a delay of 2 to 4 seconds
        time.sleep(random.randint(2, 4))
        # Yield a random moisture level between 0 and 101
        yield random.randint(0, 101)



# take the action according to the moisture level
for moisture in moisture_level():
    print("Moisture Level:", moisture)
    moistureLevel = MoistureSensor(moisture)
    wateringController = WateringController(moistureLevel)

    action  = wateringController.decideAction()
    print("Agent decided to: ", action)
