def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[93]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[a:b]]
    missing_sum = sum(missing_numbers)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]