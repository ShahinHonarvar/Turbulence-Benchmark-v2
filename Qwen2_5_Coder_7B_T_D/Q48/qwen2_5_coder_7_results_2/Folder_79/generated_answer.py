def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(tup[a + 1:b])
    if missing_numbers:
        total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()