def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[18:88]:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]