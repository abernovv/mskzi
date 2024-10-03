
def DDT(arr_in):
    print(f"Уравнения:")
    arr_out = [[0] * len(arr_in) for _ in range(len(arr_in))]
    print(f"a \ x | ", end="")
    for i in range(len(arr_in)):
        print(f"{i} ", end="")
    print("\n"+len("a \ b | ")*"-"+"-"*(len(arr_in))*2)
    for a in range(1, len(arr_in)):
        print(f"a = {a} | ", end="")
        for x in range(0, len(arr_in)):
            b = (arr_in[x] ^ arr_in[x ^ a])         # свою функцию пиши тут
            print(f"{b} ", end="")
            arr_out[a][b] += 1
        print()
    print()

    print(f"DDT:")
    print(f"a \ b | ", end="")
    for i in range(1, len(arr_in)):
        print(f"{i} ", end="")
    print("\n"+len("a \ b | ")*"-"+"-"*(len(arr_in)-1)*2)
    for a in range(1, len(arr_in)):
        print(f"a = {a} | ", end="")
        for b in range(1, len(arr_in)):
            print(f"{arr_out[a][b]} ", end="")
        print()
    return arr_out


if __name__ == '__main__':
    s = [3,0,7,6,1,4,2,5]                         # свою подстановку(нижний ряд) пиши тут
    y = DDT(s)
    #print(y)

