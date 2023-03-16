N = int(input('Введите количество монет '))
eagle = tails = 0
for i in range (N):
    x = int(input('Орел(1) или Решка(0)? '))
    if x == 1:
        eagle += 1
    else:
        tails += 1
if eagle < tails:
    print(f'Переверните {eagle} монет с орла на решку, их меньше всего')
elif eagle == tails:
    print(f'Количество орлов и решек одинаково, по {eagle} штук')
else:
    ((f'Переверните {tails} монет с решки на орла, их меньше всего'))