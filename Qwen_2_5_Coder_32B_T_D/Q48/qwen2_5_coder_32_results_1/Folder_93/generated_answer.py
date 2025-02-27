def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    expected_set = set(range(a + 1, b))
    actual_set = set(t[58:85])
    missing_set = expected_set - actual_set
    s = sum(missing_set)
    if not missing_set:
        return ''
    elif s % 2:
        return format(s, 'b')
    else:
        return format(s, 'x')