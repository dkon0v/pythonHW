import pandas as pd
import numpy as np
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame с нужными названиями столбцов
unique_vals = np.unique(data['whoAmI'])
one_hot = pd.DataFrame(columns=unique_vals)

# Заполняем one hot DataFrame единицами и нулями
for col in one_hot.columns:
    one_hot[col] = (data['whoAmI'] == col).astype(int)

# Объединяем one hot кодирование со старым DataFrame
data = pd.concat([data, one_hot], axis=1)

# Удаляем столбец "whoAmI", так как мы его уже закодировали
data = data.drop('whoAmI', axis=1)

# Печатаем результат
print(data.head())