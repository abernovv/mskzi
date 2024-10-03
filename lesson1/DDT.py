def DDT(arr_in):
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


if __name__ == '__main__':
    s = [3, 0, 7, 6, 1, 4, 2, 5]                         # свою подстановку(нижний ряд) пиши тут
    y = DDT(s)
    #print(y)

