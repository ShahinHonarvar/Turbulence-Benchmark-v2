def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    if a + 1 >= b - 1:
        return ''
    total_sum = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]