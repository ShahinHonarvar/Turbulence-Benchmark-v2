def return_binary_or_hexa(tup):
    a = tup[35]
    b = tup[64]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[a:b]]
    if missing_numbers:
        total_sum += sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()