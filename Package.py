class Package:

    # Initialize a new Package object
    def __init__(self, id, address, city, state, zip, delivery_deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    # Give a print format for Package objects
    def __str__(self):
        # If the package does not have notes, do not try to print the notes
        if (self.notes != ""):
            return "{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, {self.weight}kg, {self.notes}, {self.status}".format(self=self)
        else:
            return "{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, {self.weight}kg, ..., {self.status}".format(
                self=self)
