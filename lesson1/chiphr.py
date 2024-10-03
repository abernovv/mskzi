def DDT_table(arr_in):                                      # DDT
    print(f"Уравнения:")
    arr_out = [[0] * len(arr_in) for _ in range(len(arr_in))]
    print(f"a \ x | ", end="")
    for i in range(len(arr_in)):
        print(f"{i} ", end="")
    print("\n"+len("a \ b | ")*"-"+"-"*(len(arr_in))*2)
    for a in range(1, len(arr_in)):
        print(f"a = {a} | ", end="")
        for x in range(0, len(arr_in)):
            b = (arr_in[x] ^ arr_in[x ^ a])                 # свою функцию пиши тут
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

def shifting(bitlist):                                      # перевод списка битов в список десятичных чисел
     out = 0
     for bit in bitlist:
         out = (out << 1) | bit
     return out

def shifting_data(arr):                                     # применение функции выше для списка списков
    out = []
    for elem in arr:
        elem = shifting(elem)
        out.append(elem)
    return out

def xor_arrs(arr1, arr2):                                   # ксор списков
    res = [[0] * len(arr1) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        res[i] = arr1[i] ^ arr2[i]
    return res

def rounds(data, keys, s, num_rounds, a_start, DDT_table):  # функция раундов
    diff_table = [[0]]
    diff_table[0] = a_start
    data1 = xor_arrs(data, a_start)
    diff = xor_arrs(data,data1)

    print("start"+f"| {data} | {data1} | {diff}")
    print("-"*(7+8+2+len(data)*8))
    for i in range(num_rounds):
        a = next(item for item in diff if item > 0)
        #print(f"round = {i+1}")
        data = xor_arrs(data, keys[i])
        data1 = xor_arrs(data1, keys[i])
        diff = xor_arrs(data, data1)
        print(f"k{i + 1}   | {data} | {data1} | {diff}")
        #print(f"Data_k = {data}")
        data = [s[j] for j in data]
        data1 = [s[j] for j in data1]
        diff = xor_arrs(data, data1)
        diff_table.append(diff)
        print(f"p{i + 1}   | {data} | {data1} | {diff}")
        #print(f"Data_p = {data}")
        print("-" * (7 + 8 + 2 + len(data) * 8))

    print("\nDiff path = ", end="")
    propability = 1
    for i in range(num_rounds):                             # вывод дифференциального пути, вычисление вероятности прохождения по такому пути
        a = next(item for item in diff_table[i] if item > 0)
        b = next(item for item in diff_table[i+1] if item > 0)
        count = DDT_table[a][b]
        all = sum(DDT_example[a])
        propability = propability * count / all
        print(f"{diff_table[i]} --{count}/{all}>> ",end="")
    print(f"{diff_table[-1]} . Propability =  {propability}")

    return data, data1, diff

def databin_to_datadec(data, keys):                         # список битов в список списков десятичных
    return [data[i:i + len(keys[0])] for i in range(0, len(data), len(keys[0]))]

if __name__ == '__main__':
    data = [1,1,1,1,1,1,1,1,1]                              # входные биты
    keys = [[5,1,2],[7,0,4],[4,3,1]]                        # ключи
    s = [3, 0, 7, 6, 1, 4, 2, 5]                            # подстановка
    a = [2, 0, 0]                                           # выбранная разница для анализа работы шифратора
    num_rounds = 3                                          # число раундов шифрования

    DDT_example = DDT_table(s)
    print()

    data = databin_to_datadec(data, keys)
    data = shifting_data(data)
    print(f"data = {data}, keys = {keys}")
    print(f"num_rounds = {num_rounds}, a = {a}, s = {s}\n")

    res = rounds(data, keys, s, num_rounds, a, DDT_example)

