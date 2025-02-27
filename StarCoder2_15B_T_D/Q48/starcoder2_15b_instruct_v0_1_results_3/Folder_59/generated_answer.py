def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    s = set(t)
    sum_val = sum(range(a + 1, b))
    sum_val -= sum((i for i in range(a + 1, b) if i in s))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    elif sum_val != 0:
        return hex(sum_val)[2:]
    else:
        return ''