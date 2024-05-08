immutable_var = (25,26,27,28)
print(immutable_var)
immutable_var = immutable_var + (29,30)
print(immutable_var)
immutable_var = immutable_var * 2
print(immutable_var)
mutable_list = [25,26,27,28]
print(mutable_list)
mutable_list[0] = 45
print(mutable_list)
mutable_list.append('Число')
print(mutable_list)
mutable_list.extend('2345')
print(mutable_list)
mutable_list.remove(28)
print(mutable_list)