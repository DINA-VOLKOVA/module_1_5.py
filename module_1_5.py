immutable_var = (1, 2, 3, 'a', 'b')
print(immutable_var)
# immutable_var [0] = 10
# print(immutable_var). Кортеж это неизменяемый аналог списка, в котором нельзя добавлять, изменять или удалять элементы.


mutable_list = [1, 2, 3, 'Hi', 'Bye']
print(mutable_list)
mutable_list [0] = 5
mutable_list [3] = 'Hello'
print(mutable_list)