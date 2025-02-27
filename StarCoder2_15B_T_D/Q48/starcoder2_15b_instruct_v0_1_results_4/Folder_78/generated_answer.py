def return_binary_or_hexa(t: tuple) -> str:
    a = t[62]
    b = t[96]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    return bin(sum_of_integers)[2:]