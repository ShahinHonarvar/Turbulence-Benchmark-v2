def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[20]
    b = tup[35]
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_missing_integers += i
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]