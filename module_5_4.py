class House():
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')



gk_1 = House('ЖК "Эльбрус"', 30)
print(House.houses_history)
gk_2 = House('ЖК "Завидное"', 15)
print(House.houses_history)
gk_3 = House('ЖК "Надежда-1"', 12)
print(House.houses_history)










