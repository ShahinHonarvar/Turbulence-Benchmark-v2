def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[85]
    existing_numbers = set(tup[58:85])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]