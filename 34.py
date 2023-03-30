def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    lines = poem.split()
    syllables = [count_syllables(word.replace('-', '')) for word in lines]
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

# Функция count_syllables считает количество слогов в слове, учитывая только гласные буквы. 
# Функция check_rhythm принимает стихотворение в виде строки и проверяет, есть ли в нем ритм. 
# Сначала она разделяет стихотворение на отдельные слова и считает количество слогов в каждом слове.
#  Затем она проверяет, все ли числа слогов одинаковы, и возвращает соответствующую строку.