def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    expected = set(range(a + 1, b))
    actual = set(numbers[276:871])
    missing = expected - actual
    total = sum(missing)
    if not missing:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()