def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    expected = set(range(a + 1, b))
    present = set(numbers[91:97])
    missing = expected - present
    if not missing:
        return ''
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]