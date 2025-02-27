def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    expected = set(range(a + 1, b))
    actual = set(numbers[43:87])
    missing = expected - actual
    if not missing:
        return ''
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]