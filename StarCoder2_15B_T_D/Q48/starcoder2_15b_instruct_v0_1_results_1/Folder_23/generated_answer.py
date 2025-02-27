def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[20]
    b = tup[36]
    sum_ab = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_ab += i
    if sum_ab % 2 == 1:
        return bin(sum_ab)[2:]
    else:
        return hex(sum_ab)[2:].upper()