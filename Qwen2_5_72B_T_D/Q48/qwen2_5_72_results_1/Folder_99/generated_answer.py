def return_binary_or_hexa(t):
    if len(t) < 669:
        return ''
    a, b = (t[427], t[669])
    full_set = set(range(a + 1, b))
    tuple_set = set(t[428:669])
    missing_sum = sum(full_set - tuple_set)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]