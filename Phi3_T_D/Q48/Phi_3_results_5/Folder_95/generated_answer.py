def return_binary_or_hexa(ints):
    a = ints[32] if len(ints) > 32 else None
    b = ints[99] if len(ints) > 99 else None
    missing_sum = sum(set(range(a + 1, b)) - set(ints[32:99] if a and b else []))
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x')