def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    t_set = set(t[60:201])
    sum_of_missing_integers = sum((i for i in range(a + 1, b) if i not in t_set))
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:].upper()