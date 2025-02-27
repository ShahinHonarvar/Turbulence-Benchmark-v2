def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    subset = set(numbers[61:200])
    total_sum = sum((num for num in range(a + 1, b) if num not in subset))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]