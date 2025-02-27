def return_binary_or_hexa(l):
    a = l[68]
    b = l[99]
    sum_val = sum(range(a + 1, b)) - sum((x for x in l if a + 1 <= x <= b - 1))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()