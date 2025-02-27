def return_binary_or_hexa(numbers):
    a = numbers[50] if len(numbers) > 50 else None
    b = numbers[92] if len(numbers) > 92 else None
    if a is None or b is None or a >= b:
        return ''
    present = set(numbers[50:93])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    return bin(missing_sum)[2:]