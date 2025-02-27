def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(t[70:201])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()