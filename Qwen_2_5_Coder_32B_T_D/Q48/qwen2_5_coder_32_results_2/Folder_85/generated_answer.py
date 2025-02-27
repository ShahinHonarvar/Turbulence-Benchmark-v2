def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    full_set = set(range(a + 1, b))
    given_set = set(t[2:8])
    missing_set = full_set - given_set
    s = sum(missing_set)
    if not missing_set:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]