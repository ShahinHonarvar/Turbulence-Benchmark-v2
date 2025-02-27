def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    expected_range = set(range(a + 1, b))
    actual_range = set(t[1:9])
    diff = expected_range - actual_range
    if not diff:
        return ''
    sum_val = sum(diff)
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    return bin(sum_val)[2:]