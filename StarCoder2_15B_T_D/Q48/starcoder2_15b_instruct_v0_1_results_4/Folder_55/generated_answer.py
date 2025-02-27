def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    total = sum(range(a + 1, b))
    sum_of_range = sum((i for i in range(a + 1, b) if i not in tup))
    if sum_of_range % 2 == 1:
        return bin(sum_of_range)[2:]
    else:
        return hex(sum_of_range)[2:].upper()