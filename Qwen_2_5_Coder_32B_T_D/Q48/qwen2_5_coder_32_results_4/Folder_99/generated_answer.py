def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    full_set = set(range(a + 1, b))
    given_set = set(t[428:669])
    diff_set = full_set - given_set
    s = sum(diff_set)
    if not diff_set:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]