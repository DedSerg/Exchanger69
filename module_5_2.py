class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
             print(f'В {self.name} этажа {new_floor} не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
            print(f'Приветствуем в {self.name}, поехали на {new_floor} этаж')

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def __len__(self):
        return self.number_of_floors

gk_1 = House('ЖК "Эльбрус"', 30)
gk_2 = House('ЖК "Завидное"', 15)
gk_1.go_to(int(15))
gk_2.go_to(int(16))
print(gk_1)
print(gk_2)
print(len(gk_1))
print(len(gk_2))
