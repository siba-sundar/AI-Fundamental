import random
import time


class CropManagementAgent:
    def __init__(self):
        self.irrigation_threshold = 40
        self.pest_control_threshold = 50

    def check_crop_conditions(self, moisture, pest_presence):
        actions = []

        if moisture < self.irrigation_threshold:
            actions.append("Irrigate crops")

        if pest_presence > self.pest_control_threshold:
            actions.append("Apply pesticides")

        if len(actions) == 0:
            actions.append("Monitor crop conditions")

        return actions, moisture, pest_presence


def generate_environmental_conditions():
    time.sleep(random.randint(2, 4))
    moisture = random.randint(0, 100)
    pest_presence = random.randint(0, 100)
    return moisture, pest_presence


def main():
    agent = CropManagementAgent()

    while True:
        moisture, pest_presence = generate_environmental_conditions()

        print("\nCurrent Conditions:")
        print("Moisture Level:", moisture)
        print("Pest Presence:", pest_presence)

        actions, moisture, pest_presence = agent.check_crop_conditions(moisture, pest_presence)

        print("Agent Actions:")
        for action in actions:
            print("-", action)

        print("----------------------------")


if __name__ == "__main__":
    main()
