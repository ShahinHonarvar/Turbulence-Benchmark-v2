def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    total_sum = sum(range(a + 1, b))
    missing_integers = set(range(a + 1, b)) - set(t[48:77])
    if missing_integers:
        total_sum += sum(missing_integers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()