def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[88]
    full_set = set(range(a + 1, b))
    given_set = set(tup[57:88])
    missing_set = full_set - given_set
    if not missing_set:
        return ''
    summation = sum(missing_set)
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]