import random


class ErrorSimulator:
    def __init__(self):
        self.errors = ["brake_failure", "engine_failure", "sensor_failure"]

    def check_errors(self, engine):
        error = random.choice(self.errors)
        if random.random() < 0.1:
            print(f"Error detected: {error}")
            if error == "brake_failure":
                engine.speed = 0
                print("Brakes failed! Stopping the vehicle.")
