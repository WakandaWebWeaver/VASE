import json


class Persistence:
    @staticmethod
    def save_state(filename, state):
        with open(filename, "w") as file:
            json.dump(state, file)
        print("Persistence: Simulation state saved.")

    @staticmethod
    def load_state(filename):
        try:
            with open(filename, "r") as file:
                state = json.load(file)
            print("Persistence: Simulation state loaded.")
            return state
        except FileNotFoundError:
            print("Persistence: No saved state found.")
            return None
