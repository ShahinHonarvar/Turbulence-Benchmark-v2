def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    sum_val = sum(range(a + 1, b)) - sum(filter(lambda x: x in range(a + 1, b), t[1:4]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()