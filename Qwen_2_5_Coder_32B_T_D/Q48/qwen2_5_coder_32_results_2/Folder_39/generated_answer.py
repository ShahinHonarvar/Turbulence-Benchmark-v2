def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers[45:91]))
    if total_sum:
        return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]
    return ''