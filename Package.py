class Package:
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

    def __str__(self):
        return "{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, {self.weight}kg, {self.notes}, {self.status}".format(self=self)
