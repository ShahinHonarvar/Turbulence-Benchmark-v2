def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    expected = set(range(a + 1, b))
    actual = set(numbers[91:200])
    missing = expected - actual
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif missing:
        return hex(total)[2:]
    return ''