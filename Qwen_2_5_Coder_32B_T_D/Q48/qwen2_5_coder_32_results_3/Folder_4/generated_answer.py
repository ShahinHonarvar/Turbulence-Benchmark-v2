def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    total_sum = 0
    present_numbers = set(numbers[50:74])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]