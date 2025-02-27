def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [x for x in range(a + 1, b) if x not in t[13:77]]
    for x in missing_numbers:
        total_sum += x
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()