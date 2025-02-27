def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in t[19:33]]
    if missing_numbers:
        total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()