from mskzi.lesson1.DDT import DDT
from mskzi.lesson2.LAT import LAT


def main():
    a = int(input("Выберите вариант:\n1 - DDT table\n2 - LAT table\n"))

    if a == 1:
        s = [3, 0, 7, 6, 1, 4, 2, 5]
        DDT(s)
    elif a == 2:
        s = [3, 0, 7, 6, 1, 4, 2, 5]
        LAT(s)


if __name__ == '__main__':
    main()