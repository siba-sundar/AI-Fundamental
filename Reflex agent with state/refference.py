from colorama import Fore, Back, Style


class ThermostatAgent:
    def __init__(self, desired_temp, tolerance):
        self.desired_temp = desired_temp
        self.tolerance = tolerance
        self.current_temp = 0
        self.heater_on = False

    def update_temperature(self, new_temp):
        self.current_temp = new_temp

    def decide_action(self):
        if self.current_temp < self.desired_temp - self.tolerance:
            self.heater_on = True
            return "Turn on heater"
        elif self.current_temp > self.desired_temp + self.tolerance:
            self.heater_on = False
            return "Turn off heater"
        else:
            return "Maintain current state"


# Simulate the agent's behavior
def main():
    agent = ThermostatAgent(desired_temp=70, tolerance=2)

    # Simulate temperature changes
    temperature_readings = [65, 68, 72, 69, 73, 70]

    for temp in temperature_readings:
        agent.update_temperature(temp)
        action = agent.decide_action()
        print(Fore.MAGENTA + f"Current temperature: {temp}°F, Action: {action}")
    print(Fore.RESET)


if __name__ == "__main__":
    main()