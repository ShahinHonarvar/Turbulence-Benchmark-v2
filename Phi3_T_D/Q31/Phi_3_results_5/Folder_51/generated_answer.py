def if_perfect_num(integers):
    perfect = False
    if len(integers) > 64 and sum((i for i in range(1, integers[64]) if integers[64] % i == 0)) == integers[64]:
        perfect = True
    return perfect