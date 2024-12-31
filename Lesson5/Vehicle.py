class Vehicle():
    def __init__(self, make, model, year, color, engine):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine

    def drive_forward(self):
        print(f"Your {self.year}, {self.make}, {self.model} is driving forward!")
    
    def drive_backward(self):
        print(f"Your {self.year}, {self.make}, {self.model} is driving backward!")

    def get_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Engine: {self.engine}")
        print("Vehicle is a car")

    def display(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("color: ", self.color)


car1 = Vehicle("Toyota", "Corolla", 2019, "Red", "V6")
car2 = Vehicle("Honda", "Civic", 2018, "Blue", "V4")

car1.drive_forward()
car2.drive_forward()