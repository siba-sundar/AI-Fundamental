import random

class ElevatorControl:
    def __init__(self, elevatorFloor, userFloor):
        self.elevatorFloor = elevatorFloor
        self.userFloor = userFloor

    def senseElevator(self):
        return self.elevatorFloor.getElevatorPosition()

    def senseUser(self):
        return self.userFloor.getUserPosition()

    def decideAction(self):
        elevatorPosition = self.senseElevator()
        userPosition = self.senseUser()

        if elevatorPosition > userPosition:
            return "Move down"
        elif elevatorPosition < userPosition:
            return "Move up"
        else:
            return "Elevator on the same floor"

class ElevatorSensor:
    def __init__(self, elevatorFloor, userPosition):
        self.elevatorFloor = elevatorFloor
        self.userPosition = userPosition

    def getElevatorPosition(self):
        return self.elevatorFloor

    def getUserPosition(self):
        return self.userPosition

elevatorFloor = random.randint(0, 25)
userFloor = random.randint(0, 25)
elevatorSensor = ElevatorSensor(elevatorFloor, userFloor)
elevatorControl = ElevatorControl(elevatorSensor, elevatorSensor)

print('Elevator Position:', elevatorSensor.getElevatorPosition())
print('User Position:', elevatorSensor.getUserPosition())
action = elevatorControl.decideAction()
print("Agent decided to:", action)
