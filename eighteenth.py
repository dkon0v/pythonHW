B = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != B or B == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число Х , с которым нужно сравнить: '))
    min = abs(X-A_num[0])
    index = 0
    for i in range (1,B):
        count = abs(X-A_num[i])
        if count < min:
            min = count
            index = i 
    print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}'    )
