def arithmetic_progression(a1, d, n):
    progression = [a1 + (i - 1) * d for i in range(1, n + 1)]
    return progression

def main():
    a1 = int(input("Введите первый элемент прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов прогрессии: "))
    progression = arithmetic_progression(a1, d, n)

    print("Арифметическая прогрессия:")
    for element in progression:
        print(element)

if __name__ == "__main__":
    main()
