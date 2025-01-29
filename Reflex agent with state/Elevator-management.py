""" Question 11. Elevator Management: Design a Reflex Agent with State for controlling an elevator system. If a
call button is pressed on a floor, the elevator should move to that floor; otherwise, it remains
 stationary. The state should store the previous state of button presses."""



class ElevatorAgent:
    def __init__(self):
        self.button_pressed = None
        self.lift_current_position = 0

    def new_button_pressed(self, new_floor):
        self.button_pressed = new_floor

    def decide_action(self):
        if  self.button_pressed is None:
            return "No button pressed, lift does not move"
        elif self.lift_current_position < self.button_pressed:
            self.lift_current_position = self.button_pressed
            return f"Lift moving up to floor {self.lift_current_position}"
        elif self.lift_current_position > self.button_pressed:
            self.lift_current_position = self.button_pressed
            return f"Lift moving down to floor {self.lift_current_position}"
        else:
            return f"Lift already at {self.lift_current_position}"


def main():
    agent = ElevatorAgent()
    button_pressed = [12, 15, 15, 0, 5, 0, 0, 7, 8, 5]

    for temp in button_pressed:
        agent.new_button_pressed(temp)
        print(agent.decide_action())


if __name__ == "__main__":
    main()
