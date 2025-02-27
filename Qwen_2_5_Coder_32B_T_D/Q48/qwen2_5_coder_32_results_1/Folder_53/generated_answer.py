def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    required_set = set(range(a + 1, b))
    existing_set = set(numbers[201:202] if 202 < len(numbers) else ())
    missing_numbers = required_set - existing_set
    total_sum = sum(missing_numbers)
    if missing_numbers:
        return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]
    return ''