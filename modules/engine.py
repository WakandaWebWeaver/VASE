class Engine:
    def __init__(self):
        self.direction = "straight"
        self.is_moving = True
        self.speed = 0
        self.fuel_level = 100.0
        self.lane = 1

    def move(self):
        self.is_moving = True
        print("Engine: Vehicle is now moving.")

    def stop(self):
        self.is_moving = False
        print("Engine: Vehicle has stopped.")

    def control_steering(self, direction):
        if direction in ["left", "right", "straight"]:
            self.direction = direction
            print(f"Engine: Steering adjusted to {direction}.")
        else:
            print("Engine: Invalid direction command.")

    def consume_fuel(self, consumption_rate):
        self.fuel_level -= consumption_rate
        if self.fuel_level < 0:
            self.fuel_level = 0
            print("Out of fuel! Please refuel.")
