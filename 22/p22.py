def find_common_elements():
    n = int(input("Введите количество элементов первого множества: "))
    m = int(input("Введите количество элементов второго множества: "))

    set1 = set()
    set2 = set()

    print("Введите элементы первого множества:")
    for i in range(n):
        num = int(input())
        set1.add(num)

    print("Введите элементы второго множества:")
    for i in range(m):
        num = int(input())
        set2.add(num)

    common_elements = set1.intersection(set2)

    common_elements_list = list(common_elements)
    common_elements_list.sort()

    print("Общие элементы в порядке возрастания:")
    for num in common_elements_list:
        print(num, end=" ")


if __name__ == "__main__":
    find_common_elements()
