def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[8]
    total_sum = 0
    present_numbers = set(numbers[1:9])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]