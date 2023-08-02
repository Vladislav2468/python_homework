def max_berries_to_collect(a):
    max_berries = 0

    for i in range(1, len(a) - 1):
        berries = a[i] + a[i - 1] + a[i + 1]
        max_berries = max(max_berries, berries)

    return max_berries

a = [5, 10, 2, 7, 15]
result = max_berries_to_collect(a)
print("Максимальное количество ягод:", result)
