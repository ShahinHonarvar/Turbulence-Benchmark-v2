def return_binary_or_hexa(numbers):
    a, _, b = numbers[:3]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]