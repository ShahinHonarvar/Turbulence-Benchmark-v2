def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[35]
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(20, 36) if a + 1 <= tup[i] <= b - 1))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()