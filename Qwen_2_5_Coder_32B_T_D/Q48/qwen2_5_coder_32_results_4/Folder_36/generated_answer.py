def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    expected_set = set(range(a + 1, b))
    given_set = set(t[111:348])
    diff_set = expected_set - given_set
    total = sum(diff_set)
    if not diff_set:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower()