from mskzi.lesson1.DDT import DDT_consol,DDT_latex
from mskzi.lesson2.LAT import LAT_consol,LAT_latex


def main():
    c_l = int(input("Выберите режим вывода:\n1 - консоль\n2 - латех\n"))
    if c_l == 1:
        a = int(input("Выберите вариант:\n1 - DDT table\n2 - LAT table\n"))
        if a == 1:
            s = [3, 0, 7, 6, 1, 4, 2, 5]
            DDT_consol(s)
        elif a == 2:
            s = [3, 0, 7, 6, 1, 4, 2, 5]
            LAT_consol(s)
            
    elif c_l == 2:
        a = int(input("Выберите вариант:\n1 - DDT table\n2 - LAT table\n"))
        if a == 1:
            s = [3, 0, 7, 6, 1, 4, 2, 5]
            DDT_latex(s)
        elif a == 2:
            s = [3, 0, 7, 6, 1, 4, 2, 5]
            LAT_latex(s)


if __name__ == '__main__':
    main()