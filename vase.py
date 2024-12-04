# Vehicle Automation/Simulation Engine

import random
import time
import colorama
from colorama import Fore

from modules.engine import Engine
from modules.bald import BALD
from modules.nice import NICE
from logs import Logs
from persistence import Persistence

colorama.init(autoreset=True)


class VASE:
    def __init__(self):
        self.engine = Engine()
        self.bald = BALD()
        self.nice = NICE()
        self.logs = Logs()
        self.position = 0
        self.dynamic_event_frequency = 5
        self.running = True

    def run(self):
        print(
            Fore.CYAN +
            "Welcome to VASE (Vehicle Automation Simulation Environment)"
        )
        while self.running:
            if not self.nice.scene.objects:
                self.nice.generate_scene("urban")
                if not self.nice.scene.objects:
                    break

            if self.position >= len(self.nice.scene.objects):
                self.position = 0

            self.start_simulation()
            self.show_dashboard()

            time.sleep(random.randint(1, 4))

    def start_simulation(self):
        if not self.nice.scene.objects:
            self.nice.generate_scene("urban")
        else:
            print(
                Fore.CYAN +
                f"Scene objects: {self.nice.scene.objects}"
            )
        if self.position % self.dynamic_event_frequency == 0:
            self.nice.inject_dynamic_events()

        condition = self.nice.check_condition(self.position)
        event = self.nice.get_dynamic_event()
        self.logs.add_entry(
            f"Position {self.position}: Condition: {condition}, Event: {event}")

        self.handle_condition(condition, event)

        self.position += 1

    def handle_condition(self, condition, event):
        if condition == "clear road":
            self.bald.accelerate()
        elif condition in ["pothole", "speed bump"]:
            self.bald.decelerate()
        elif condition == "red signal":
            self.stop_vehicle()

        if event == "accident":
            print(
                Fore.RED + "Dynamic Event: Accident! Emergency brake applied."
            )
            self.bald.emergency_brake()
        elif event == "heavy rain":
            print(
                Fore.RED + "Dynamic Event: Heavy rain! Speed reduced."
            )
            self.bald.decelerate()

    def stop_vehicle(self):
        self.engine.stop()
        self.bald.decelerate()

    def show_dashboard(self):
        speed = self.bald.speed
        speed_indicator = self.get_speed_indicator(speed)

        print(
            Fore.CYAN +
            "\nDashboard:"
        )
        print(
            Fore.CYAN +
            f"Speed: {speed} km/h {speed_indicator}"
        )
        print(
            Fore.CYAN +
            f"Position: {self.position}"
        )
        print(
            Fore.CYAN +
            f"Weather: {self.nice.scene.weather}"
        )
        print(
            Fore.CYAN +
            f"Traffic Density: {self.nice.scene.traffic_density}"
        )
        print(
            Fore.CYAN +
            "-" * 40
        )

    def get_speed_indicator(self, speed):
        max_speed = 100
        filled = int(speed / max_speed * 20)
        empty = 20 - filled
        return f"[{'#' * filled}{'.' * empty}]"

    def save_state(self):
        state = {
            "position": self.position,
            "speed": self.bald.speed,
            "direction": self.engine.direction,
            "scene": self.nice.scene.objects
        }
        Persistence.save_state("simulation_state.json", state)

    def load_state(self):
        state = Persistence.load_state("simulation_state.json")
        if state:
            self.position = state["position"]
            self.bald.speed = state["speed"]
            self.engine.direction = state["direction"]
            self.nice.scene.objects = state["scene"]


if __name__ == "__main__":
    vase = VASE()
    vase.load_state()
    vase.run()
    vase.save_state()
