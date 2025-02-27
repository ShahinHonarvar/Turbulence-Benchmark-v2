def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    present_numbers = set(t[11:76])
    missing_sum = sum((n for n in range(a + 1, b) if n not in present_numbers))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]