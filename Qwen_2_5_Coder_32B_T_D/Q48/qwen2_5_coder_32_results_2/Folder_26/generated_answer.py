def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    full_set = set(range(a + 1, b))
    given_set = set(t[69:99])
    missing_set = full_set - given_set
    s = sum(missing_set)
    if not missing_set:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]