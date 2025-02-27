def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[111:348]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]