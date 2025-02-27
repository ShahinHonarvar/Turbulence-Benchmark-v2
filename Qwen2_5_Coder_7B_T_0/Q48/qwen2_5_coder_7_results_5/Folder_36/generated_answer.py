def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(t[110:349])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()