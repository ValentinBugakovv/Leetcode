"""
1.Напишите функцию, которая принимает на вход массив чисел и возвращает 2 максимальных элемента.
Оцените сложность алгоритма по времени и по памяти в терминах “big O notation”.
"""

example_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_to_max(lst: list[int]) -> tuple[int, int]:
    max1 = float("-inf")
    max2 = float("-inf")

    for num in lst:
        if max1 < num:
            max2 = max1
            max1 = num
        elif max1 > num:
            max2 = num

    return max1, max2


result = get_to_max(example_lst)
print(result)

# Скорость O(n)
# Память O(1)
