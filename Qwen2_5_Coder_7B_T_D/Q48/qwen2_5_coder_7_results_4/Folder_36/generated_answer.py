def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    total_sum = sum(range(a + 1, b)) - sum([x for x in range(a + 1, b) if x in t[110:349]])
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()