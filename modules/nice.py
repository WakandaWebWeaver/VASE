# Navigational Ingenuity Control Engine


class Scene:
    def __init__(self):
        self.objects = []
        self.weather = "clear"
        self.traffic_density = "light"

    def __len__(self):
        return len(self.objects)

    def load_scene(self, scene_file):
        with open(f"scenes/{scene_file}", "r") as file:
            self.objects = [line.strip() for line in file.readlines()]
        print(f"Loaded scene: {scene_file}")

    def add_obstacle(self, obstacle):
        self.objects.append(obstacle)
        print(f"Added obstacle: {obstacle}")

    def remove_obstacle(self, obstacle):
        if obstacle in self.objects:
            self.objects.remove(obstacle)
            print(f"Removed obstacle: {obstacle}")


class NICE:
    def __init__(self):
        self.scene = Scene()

    def generate_scene(self, scene_type):
        print(f"Generating {scene_type} scene...")
        if scene_type == "urban":
            self.scene.load_scene("urban.txt")
        elif scene_type == "rural":
            self.scene.load_scene("rural.txt")
        elif scene_type == "highway":
            self.scene.load_scene("highway.txt")
        else:
            print("Unknown scene type.")

        print(f"Scene objects after generation: {self.scene.objects}")

    def load_scene(self, scene_file):
        try:
            with open(f"scenes/{scene_file}", "r") as file:
                self.objects = [line.strip() for line in file.readlines()]
                if not self.objects:
                    print(
                        f"Warning: {scene_file} is empty or doesn't contain obstacles.")
                print(f"Loaded scene from {scene_file}: {self.objects}")
        except FileNotFoundError:
            print(f"Error: Scene file {scene_file} not found.")
            self.objects = []

    def inject_dynamic_events(self):
        import random
        events = ["accident", "roadblock", "heavy rain", "speed bump",
                  "protest", "vehicle breakdown", "construction", "fog"]
        event = random.choice(events)
        self.scene.add_obstacle(event)
        print(f"Dynamic Event: {event}")

    def check_condition(self, position):
        if position % 5 == 0:
            return "pothole"
        elif position % 3 == 0:
            return "red signal"
        else:
            return "clear road"

    def get_dynamic_event(self):
        self.inject_dynamic_events()
        return self.scene.objects[-1]
