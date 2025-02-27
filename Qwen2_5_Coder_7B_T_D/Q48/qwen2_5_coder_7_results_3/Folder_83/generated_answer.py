def return_binary_or_hexa(t):
    a = t[90]
    b = t[200]
    sum_val = sum(range(a + 1, b))
    missing_nums = [x for x in range(a + 1, b) if x not in t[90:201]]
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]