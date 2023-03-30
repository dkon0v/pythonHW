def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печатаем заголовок таблицы
    print("    ", end="")
    for j in range(1, num_columns+1):
        print("{:>8}".format(j), end="")
    print()
    # Печатаем разделительную линию
    print("  +", "-"*8*num_columns, sep="")
    # Печатаем содержимое таблицы
    for i in range(1, num_rows+1):
        print("{:>2} |".format(i), end="")
        for j in range(1, num_columns+1):
            value = operation(i, j)
            print("{:>8.2f}".format(value), end="")
        print()


# Как это работает:

# Сначала мы печатаем заголовок таблицы, который содержит номера столбцов. Мы используем end="" в вызове print для того, 
# чтобы выводить каждое следующее значение в той же строке, а не начинать новую строку.
# Наконец, мы печатаем содержимое таблицы, используя циклы for для прохода по строкам и столбцам.
#  Мы вызываем функцию operation для вычисления значения элемента таблицы и форматируем его с помощью метода format, 
# чтобы он имел ширину 8 символов и два знака после запятой.

