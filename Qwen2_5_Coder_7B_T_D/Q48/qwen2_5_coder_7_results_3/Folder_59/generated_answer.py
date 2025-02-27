def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[10])
    total_sum = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in tup]
    if missing_numbers:
        total_sum -= sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]