class Dashboard:
    def __init__(self):
        pass

    def update(self, engine, scene, weather):
        print(
            f"Speed: {engine.speed} km/h | Fuel: {engine.fuel_level}% | Weather: {weather.weather_conditions}")
        print(f"Current Scene Objects: {scene.objects}")
