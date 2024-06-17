class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'В {self.name} этажа {new_floor} не существует')
        else:
            print(f'Приветствуем в {self.name}, поехали на {new_floor} этаж')
gk_1 = House('ЖК "Эльбрус"', 30)
gk_2 = House('ЖК "Завидное"', 15)
print(gk_1.go_to(int(input())))
print(gk_2.go_to(int(input())))