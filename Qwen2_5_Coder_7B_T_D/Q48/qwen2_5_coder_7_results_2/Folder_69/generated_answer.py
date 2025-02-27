def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    total = sum(range(a + 1, b))
    excluded = sum((t[i] for i in range(39, 44)))
    actual_sum = total - excluded
    if actual_sum % 2 == 0:
        return hex(actual_sum)[2:].upper()
    else:
        return bin(actual_sum)[2:]