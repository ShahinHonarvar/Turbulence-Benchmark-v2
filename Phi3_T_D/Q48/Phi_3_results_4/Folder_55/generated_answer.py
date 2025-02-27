def return_binary_or_hexa(numbers):
    a, _, b, _ = numbers[10:12] + [None, None]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[10:12]))
    representation = bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()
    return representation