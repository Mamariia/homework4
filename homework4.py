immutable_var = 1, 2, 'string', True, [0,1,2,3]
print(immutable_var)
print(immutable_var[2])
print(immutable_var[0:2])

# immutable_var[0] = 3
# Кортеж является неизменяемым типом данных, поэтому при запуске команды выше программа выдаст ошибку.
immutable_var[4][1] = 5
print(immutable_var)
# Но несмотря на это, кортеж может содержать изменяемые элементы, такие как список.
# Команда выше заменила 2й элемент в списке, который входит в кортеж.

mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 9
mutable_list[3] = 'string'
mutable_list.append(True)
print(mutable_list)
