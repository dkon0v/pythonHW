P = abs(int(input('Введите количество элементов из списка А ')))
A_entered = input('Введите через пробелт элементы   списка : ').split()
A_numbers = list(map(int, A_entered))
if len(A_numbers) != P:
    print('Введенные элементы не соответсвуют необходимому количеству.')
else:
    x = int(input('Введите число X,которое необходимо найти в списке '))
    count = 0 
    for i in range(P):
        if A_numbers[i] == x:
            count += 1
    print (f'Число {x} встречается в списке A {count} раз')