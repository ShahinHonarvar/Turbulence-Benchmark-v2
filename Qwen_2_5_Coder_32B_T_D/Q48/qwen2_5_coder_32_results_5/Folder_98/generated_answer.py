def return_binary_or_hexa(numbers):
    a, b = (numbers[6], numbers[7])
    total_sum = 0
    numbers_set = set(numbers[6:8])
    for num in range(a + 1, b):
        if num not in numbers_set:
            total_sum += num
    if total_sum % 2:
        return bin(total_sum)[2:]
    elif total_sum:
        return hex(total_sum)[2:]
    return ''