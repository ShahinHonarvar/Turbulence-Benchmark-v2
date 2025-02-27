def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(b) if i not in t[slice(57, 85)]))
    if actual_sum < expected_sum:
        representation = format(actual_sum, 'b')
    else:
        representation = format(actual_sum, 'x')
    return representation