class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self,model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self._Car__is_valid_vin(__vin)
        self._Car__is_valid_numbers(__numbers)


    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if type(self.vin_number) != int:
            raise IncorrectVinNumber('Некорректный тип vin номер')
            return
        if self.vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return
        if type(self.vin_number) == int and self.vin_number in range(1000000, 9999999):
            return True


    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if type(self.numbers) != str:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            return
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
            return
        if type(self.numbers) == str and len(self.numbers) == 6:
            return True
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
