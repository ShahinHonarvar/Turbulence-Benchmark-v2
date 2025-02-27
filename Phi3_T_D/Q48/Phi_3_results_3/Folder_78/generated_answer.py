def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum(set(range(a + 1, b)) - set(t[62:97]))
    if actual_sum:
        if actual_sum % 2:
            return bin(actual_sum)[2:]
        else:
            return hex(actual_sum)[2:]
    return ''