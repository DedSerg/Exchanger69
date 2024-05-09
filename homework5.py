my_list = ['кролик','овца','свинья','корова','лошадь']
my_string = "Первый элемент: "
print(my_string,my_list[0])
new_string = "Последний элемент: "
print(new_string,my_list[-1])
print(my_list[2:])
my_list[2] = 'курица'
print(my_list)
my_dict = {'кролик':'rabbit','овца':'sheep','свинья':'pig','корова':'cow', 'лошадь':'horse'}
print(my_dict)
print(my_dict['кролик'])
my_dict[('кролик')] = 'rat'
print(my_dict)


