def return_binary_or_hexa(t: tuple) -> str:
    a = t[56]
    b = t[90]
    s = set(t[56:91])
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in s:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].lstrip('0')
    else:
        return bin(sum_of_integers)[2:].lstrip('0')