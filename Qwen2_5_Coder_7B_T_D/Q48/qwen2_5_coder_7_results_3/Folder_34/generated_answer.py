def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[200]
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(61, 200) if a + 1 <= tup[i] <= b - 1))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]