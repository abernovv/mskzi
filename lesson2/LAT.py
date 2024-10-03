import math


def dot(v1, v2):
    if len(v1) != len(v2):
        raise ValueError
    return sum(i1*i2 for i1, i2 in zip(v1, v2)) % 2


def dec_to_bitarr(dec_num, size):
    return [int(x) for x in '{:0{size}b}'.format(dec_num, size=size)]


def LAT(s):
    temp = len(s)
    size = int(math.log2(temp))
    res = [[0] * len(s) for _ in range(len(s))]

    for a in range(len(s)):
        for b in range(len(s)):
            count = 0
            for x in range(len(s)):
                if (dot(dec_to_bitarr(x, size), dec_to_bitarr(a, size)) ==
                        dot(dec_to_bitarr(b, size), dec_to_bitarr(s[x], size))):
                    count += 1

                print(
                    f"α={a}, β={b}, x={x}| {dec_to_bitarr(x, size)} xor {dec_to_bitarr(a, size)} = {dot(dec_to_bitarr(x, size), dec_to_bitarr(a, size))} | {dec_to_bitarr(b, size)} xor {dec_to_bitarr(s[x], size)} = {dot(dec_to_bitarr(b, size), dec_to_bitarr(s[x], size))}. Is equal: {dot(dec_to_bitarr(x, size), dec_to_bitarr(a, size)) == dot(dec_to_bitarr(b, size), dec_to_bitarr(s[x], size))}")
            print("-" * 84)

            res[a][b] = abs((2 * count / pow(2, size)) - 1)
            # print(f"a={a}, b={b}, count={count}, m={len(s)}, res={res[a][b]}")

    print("LAT table")
    print("α \\ β")
    for elem in res:
        print(elem)


if __name__ == '__main__':
    s = [3, 0, 7, 6, 1, 4, 2, 5]
    LAT(s)