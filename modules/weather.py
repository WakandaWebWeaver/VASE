class Weather:
    def __init__(self):
        self.weather_conditions = "clear"

    def update_weather(self, scene):
        if "rain" in scene.objects:
            self.weather_conditions = "rain"
            print("Weather changed: Rainy conditions.")
        elif "fog" in scene.objects:
            self.weather_conditions = "fog"
            print("Weather changed: Foggy conditions.")
        else:
            self.weather_conditions = "clear"
