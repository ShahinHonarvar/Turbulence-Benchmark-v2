def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    sum_of_ints = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_of_ints += i
    if sum_of_ints % 2 == 1:
        return bin(sum_of_ints)[2:]
    else:
        return hex(sum_of_ints)[2:].lower()