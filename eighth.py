a,b,c = int(input('Введите первую сторону: ')), int(input('Введите вторую сторону: ')), int(input('Введите количество долек: '))
if c%a == 0 or c%b == 0:
    print('Да')
else:
    print('Нет')