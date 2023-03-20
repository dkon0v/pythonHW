from random import randint
a_set = set(randint(1,20) for i in range(int(input('Введите количество элементов первого множества :'))))
print(a_set)
b_set = set(randint(1,20) for i in range(int(input('Введите количество элементов второго множества :'))))
print(b_set)
c_set = sorted(a_set.inserction(b_set))
print(c_set)
