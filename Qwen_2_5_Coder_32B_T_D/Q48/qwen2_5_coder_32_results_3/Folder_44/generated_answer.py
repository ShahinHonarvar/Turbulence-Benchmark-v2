def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[52])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for i, x in enumerate(tup) if 36 < i < 52 and a < x < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]