import random
from colorama import Fore, Back, Style
class ReflexAgent:
    def __init__(self, light_sensor):
        self.light_sensor = light_sensor

    def sense_light(self):
        # Simulate reading the light sensor's value
        return self.light_sensor.get_light_intensity()

    def decide_action(self):
        light_intensity = self.sense_light()

        if light_intensity < 0.5:  # It's dark
            return "Turn On"
        else:  # It's bright
            return "Turn Off"

class LightSensor:
    def __init__(self, light_intensity):
        self.light_intensity = light_intensity

    def get_light_intensity(self):
        return self.light_intensity

# Simulate the environment
light_sensor = LightSensor(light_intensity= random.random())
print(Fore.MAGENTA + 'light intensity:', light_sensor.light_intensity)
reflex_agent = ReflexAgent(light_sensor)

# Run the agent
action = reflex_agent.decide_action()
print( "Agent decided to:", action)
print(Fore.RESET)