def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[10]
    b = tup[97]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers).replace('0b', '')
    else:
        return hex(sum_of_integers).replace('0x', '')