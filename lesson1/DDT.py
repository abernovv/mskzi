def DDT_consol(arr_in):
    print(f"Уравнения:\nΠ(x) ⊕ Π(x⊕α) = β")
    print(f"α \\ x |", " ".join(map(str, range(0, len(arr_in)))))
    print((len("α \\ b | ")+(len(arr_in))*2) * "-")

    arr_out = [[0] * len(arr_in) for _ in range(len(arr_in))]
    for a in range(1, len(arr_in)):
        print(f"α = {a} | ", end="")
        for x in range(0, len(arr_in)):
            b = (arr_in[x] ^ arr_in[x ^ a])         # свою функцию пиши тут
            print(f"{b} ", end="")
            arr_out[a][b] += 1
        print()

    print("\nDDT:")
    print(f"α \\ β |", " ".join(map(str, range(1, len(arr_in)))))
    print((len("a \\ β | ") + (len(arr_in)-1)*2) * "-")
    for a in range(1, len(arr_in)):
        print(f"α = {a} | ", end="")
        print(" ".join(str(arr_out[a][b]) for b in range(1, len(arr_in))))

    return arr_out


def DDT_latex(arr_in):

    print("\\begin{table}[h]\n\\centering\n\\begin{tabular}{c|"+"c"*len(arr_in) + "}")
    print("α / x &", " & ".join(map(str, range(0, len(arr_in)))), "\\\\\\hline")
    arr_out = [[0] * len(arr_in) for _ in range(len(arr_in))]
    for a in range(1, len(arr_in)):
        print(f"{a} ", end="")
        for x in range(0, len(arr_in)):
            b = (arr_in[x] ^ arr_in[x ^ a])         # свою функцию пиши тут
            print(f" & {b}", end="")
            arr_out[a][b] += 1
        print("\\\\")
    print("\\end{tabular}\n\\caption{Π(x) $\\oplus$ Π(x$\\oplus$α) = β таблица}\n"
          "\\label{tab:Π(x) $\\oplus$ Π(x$\\oplus$α) = β таблица}\n\\end{table}\n")


    print("\\begin{table}[h]\n\\centering\n\\begin{tabular}{c|" + "c"*(len(arr_in)-1) + "}")
    print(f"α / β &", "&".join(map(str, range(1, len(arr_in)))), end="\\\\\\hline\n")
    for a in range(1, len(arr_in)):
        print(f" {a} & ", end="")
        print("&".join(str(arr_out[a][b]) for b in range(1, len(arr_in))),end="\\\\\n")
    print("\\end{tabular}\n\\caption{DDT таблица}\n\\label{tab:DDT таблица}\n\\end{table}\n")
    return arr_out


if __name__ == '__main__':
    s = [3, 0, 7, 6, 1, 4, 2, 5]                         # свою подстановку(нижний ряд) пиши тут
    y = DDT_consol(s)
    #print(y)

