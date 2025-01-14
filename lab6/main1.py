class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'Вы выбрали автомобиль {self.make} {self.model}'

class Car(Vehicle):
    fuel_type = 'АИ-95'
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f'{super().get_info()}, который заправляется {self.fuel_type}'


car_1 = Car('Лада', 'Веста', 'AИ-92')
print(car_1.get_info())
