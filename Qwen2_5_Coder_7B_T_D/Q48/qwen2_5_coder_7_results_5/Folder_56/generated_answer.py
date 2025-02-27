def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    total_sum = sum((i for i in range(a + 1, b) if i not in t[7:10]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()