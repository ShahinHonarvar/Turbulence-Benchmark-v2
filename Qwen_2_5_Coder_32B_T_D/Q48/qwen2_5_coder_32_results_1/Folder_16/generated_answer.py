def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    total_sum = 0
    available_numbers = set(numbers[91:97])
    for num in range(a + 1, b):
        if num not in available_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]