def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    existing_numbers = set(numbers[91:200])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in existing_numbers:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]