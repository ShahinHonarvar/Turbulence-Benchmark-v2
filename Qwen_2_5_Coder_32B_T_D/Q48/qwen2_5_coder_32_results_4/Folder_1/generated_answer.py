def return_binary_or_hexa(tup):
    a = tup[17]
    b = tup[88]
    full_set = set(range(a + 1, b))
    present_set = set(tup[18:88])
    missing_set = full_set - present_set
    if not missing_set:
        return ''
    missing_sum = sum(missing_set)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]