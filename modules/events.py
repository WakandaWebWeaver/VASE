class Events:
    def __init__(self):
        self.events = []

    def check_events(self, scene):
        for event in self.events:
            if event == "accident":
                print("Accident detected on the road!")
                scene.add_obstacle("Accident")
            elif event == "pothole":
                print("Pothole detected!")
                scene.add_obstacle("Pothole")
            elif event == "speed bump":
                print("Speed bump detected!")
                scene.add_obstacle("Speed bump")
            elif event == "heavy rain":
                print("Heavy rain detected!")
                scene.add_obstacle("Heavy rain")
            elif event == "protest":
                print("Protest detected!")
                scene.add_obstacle("Protest")
            elif event == "vehicle breakdown":
                print("Vehicle breakdown detected!")
                scene.add_obstacle("Vehicle breakdown")
            elif event == "construction":
                print("Construction detected!")
                scene.add_obstacle("Construction")

    def trigger_event(self, event_command):
        event = event_command.split(" ")[1]
        self.events.append(event)
        print(f"Event triggered: {event}")
