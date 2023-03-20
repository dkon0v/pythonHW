from random import randint
list_one = list(randint(1,5) for i in range (int(input('Введите количество кустов: '))))
print(list_one) 
n = int(input('Введите номер куста: '))
res = 0
if n == 1:
    res = list_one[0] + list_one[1] + list_one[-1]
elif n == len(list_one):
    res = list_one[-2] + list_one[-1] + list_one[0]
else:
    res = list_one[n-1] + list_one[n-2] + list_one[n]
print (res, ' ягод ')