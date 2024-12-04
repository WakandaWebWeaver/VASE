class Traffic:
    def __init__(self):
        self.traffic_density = "light"

    def update_traffic(self, scene):
        self.traffic_density = "heavy" if "traffic_jam" in scene.objects else "light"
        print(f"Traffic density is {self.traffic_density}")
