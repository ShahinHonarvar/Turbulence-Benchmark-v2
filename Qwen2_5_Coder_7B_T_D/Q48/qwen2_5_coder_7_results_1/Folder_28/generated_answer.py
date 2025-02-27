def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    total_sum = sum(range(a + 1, b)) - sum((t[i] for i in range(86, 100)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()