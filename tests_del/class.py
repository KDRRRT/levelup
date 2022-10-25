class car:
    def __init__(self, colour, name, run):
        self.colour = colour
        self.name = name
        self.run = run

    def print_ride(self):
        n = int(input("Сколько Вы проехали?"))
        self.run += n
        print(f"автомобиль {self.name} цвета {self.colour} проехал {self.run} километров")


car1 = car("черный", "Honda", 1000)
car2 = car("фуксия", "BMW", 1500)
car3 = car("белый", "Suzuki", 10)

car1.print_ride()
car2.print_ride()
car3.print_ride()
