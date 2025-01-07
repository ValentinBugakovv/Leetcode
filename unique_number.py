"""Последовательность с повторами
Дан массив чисел, в котором все числа встречаются дважды, кроме одного числа, которое встречается только один раз.
 Напишите функцию на Python, которая найдет это уникальное число в массиве.
  Укажите оценку сложности алгоритма в O-нотации. Если используете сортировку или словари, объясните, как они работают внутри.
"""

from collections import defaultdict


example_list = [2, 1, 4, 2, 1, 5, 5, 6, 7, 6, 7]


def get_unique_num(lst: list[int]) -> int:
    number_dict = {}  # noqa: F841

    for num in lst:
        if num not in number_dict:
            number_dict[num] = 1
        else:
            number_dict[num] += 1

    number = sorted(number_dict.items(), key=lambda x: x[1])[0][0]

    return number


print(get_unique_num(example_list))


# Решенеие через дефолт дикт
def get_unique_num(lst: list[int]) -> int:
    number_dict = defaultdict(int)

    for num in lst:
        number_dict[num] += 1

    number = sorted(number_dict.items(), key=lambda x: x[1])[0][0]

    return number


print(get_unique_num(example_list))

from collection import defaultdict

def f(arr: list) -> int:
    dct = defaultdict(int) 
    
    for val in arr:
        dct[val] += 1 #{1: 2, 4: 1}
    
    for key, val in dct.items(): 
        if val == 1: 
            return key # O(n)

def find_unique_xor(arr: list[int]) -> int:
    result = 0
    for num in arr:
        result ^= num
    return result
