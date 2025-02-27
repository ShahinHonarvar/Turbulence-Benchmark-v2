def return_binary_or_hexa(tup):
    a = tup[40]
    b = tup[200]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in tup]
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return ''