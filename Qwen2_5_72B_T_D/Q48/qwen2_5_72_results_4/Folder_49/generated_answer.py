def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    subset = set(numbers[81:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]