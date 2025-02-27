def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    s = set(t)
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in s:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    else:
        return bin(sum_of_integers)[2:]