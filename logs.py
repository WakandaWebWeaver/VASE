class Logs:
    def __init__(self):
        self.log = []

    def add_entry(self, message):
        self.log.append(message)
        print(f"Log: {message}")
