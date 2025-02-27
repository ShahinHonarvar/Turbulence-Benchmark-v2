def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(t[a + 1:b])
    if missing_numbers:
        total_sum -= sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()