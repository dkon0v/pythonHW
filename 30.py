# Этот код запрашивает у пользователя первый элемент, разность и количество элементов прогрессии. 
# Затем он использует цикл for для вычисления каждого элемента прогрессии с помощью формулы 
# an = a1 + (n-1) * d и добавляет каждый элемент в список, названный прогрессия. 
# Наконец, он выводит список элементов прогрессии.



a1 = float(input("Enter the first element: "))
d = float(input("Enter the common difference: "))
n = int(input("Enter the number of elements: "))

progression = []

for i in range(n):
    progression.append(a1 + i * d)

print(progression)