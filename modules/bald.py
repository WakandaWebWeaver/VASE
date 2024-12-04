# Braking, Accelerating, Locomotion Driver

class BALD:
    def __init__(self):
        self.speed = 0
        self.brake_fail = False

    def accelerate(self, increment=10):
        if not self.brake_fail:
            self.speed += increment
            print(f"BALD: Accelerating. Speed is now {self.speed} km/h.")
        else:
            print("BALD: Unable to accelerate properly due to brake failure!")

    def decelerate(self, decrement=15):
        if not self.brake_fail:
            self.speed -= decrement
            if self.speed < 0:
                self.speed = 0
            print(f"BALD: Decelerating. Speed is now {self.speed} km/h.")
        else:
            print("BALD: Brake failure! Unable to decelerate.")


class BaldControl:
    def __init__(self):
        pass

    def control_speed(self, current_speed, traffic):
        """
        Adjust the vehicle speed based on traffic density.
        :param current_speed: Current speed of the vehicle.
        :param traffic: Traffic object containing traffic density.
        :return: Adjusted speed based on traffic conditions.
        """
        if traffic.traffic_density == "heavy":
            return max(0, current_speed - 5)
        elif traffic.traffic_density == "moderate":

            return max(0, current_speed - 2)
        return current_speed


class BALD:
    def __init__(self):
        self.speed = 0
        self.direction = "straight"
        self.bald_control = BaldControl()

    def accelerate(self):
        """Increase vehicle speed."""
        self.speed += 5
        print(f"Accelerating. Current speed: {self.speed} km/h.")

    def decelerate(self):
        """Decrease vehicle speed."""
        self.speed = max(0, self.speed - 5)
        print(f"Decelerating. Current speed: {self.speed} km/h.")

    def emergency_brake(self):
        """Emergency braking."""
        self.speed = 0
        print("Emergency brake applied! Vehicle stopped.")

    def control_speed(self, traffic):
        """Control the speed based on traffic conditions."""
        self.speed = self.bald_control.control_speed(self.speed, traffic)
        print(f"Current speed adjusted for traffic: {self.speed} km/h.")
