def return_binary_or_hexa(values):
    a, b = set(values[90:98])
    missing_sum = sum((i for i in range(a + 1, b) if i not in a))
    representation = bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]
    if representation:
        if representation.startswith('0'):
            representation = representation[1:]
        return representation
    return ''