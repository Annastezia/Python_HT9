# 5. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

import random

my_str = [int(random.randint(0, 10)) for i in range(1, 20)]
print(my_str)

def count(my_str):
    dict= {int(item):my_str.count(item) for item in my_str}
    sorted = sorted(dict.items(), key=lambda item: item[1])
    return dict(sorted[-3:])

print(count(my_str))