import pickle


class StateManager:
    def save_state(self, engine, scene):
        state = {"engine": engine.__dict__, "scene": scene.__dict__}
        with open("simulation_state.pkl", "wb") as f:
            pickle.dump(state, f)
        print("State saved.")

    def load_state(self):
        try:
            with open("simulation_state.pkl", "rb") as f:
                state = pickle.load(f)
            print("State loaded.")
            return state
        except FileNotFoundError:
            print("No saved state found.")
            return None
