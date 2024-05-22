def print_params (a = 5, b = 'Это весна, Маугли', c = True):
    print(a, b, c)

print_params(5, 'Это весна, Маугли', True)

values_list = [5, 'Это весна, Маугли', True]
values_dict = {'a': 5, 'b': 'Это весна, Маугли', 'c': True}
def print_params (*values_list):
    print(*values_list)
print_params(*values_list)

def print_params (a, b, c):
        print(a, b, c)
print_params(**values_dict)

values_list_2 = [25, 'Шерхан']
def print_params (*values_list_2):
    print(*values_list_2)

print_params(*values_list_2, 42)


