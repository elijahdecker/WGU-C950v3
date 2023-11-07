class Truck:

    # Initialize a new Truck object
    def __init__(self, name, speed, current_time, packages, current_location):
        self.name = name
        self.speed = speed
        self.current_time = current_time
        self.packages = packages
        self.current_location = current_location
        self.distance = 0.0
