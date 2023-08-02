import random

def find_indixes(lst, min_val, max_val):
    result = []
    for i, num in enumerate(lst):
        if min_val <= num <= max_val:
            result.append(i)
    return result

random_list = [random.randint(-100, 100) for _ in range(10)]
print("Список:", random_list)

min_val = int(input("Минимальное значение диапазона: "))
max_val = int(input("Максимальное значение диапазона: "))

indices = find_indixes(random_list, min_val, max_val)
print(indices)
