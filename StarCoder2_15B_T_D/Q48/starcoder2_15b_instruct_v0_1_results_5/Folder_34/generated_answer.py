def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[200]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in tup[60:201]:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()