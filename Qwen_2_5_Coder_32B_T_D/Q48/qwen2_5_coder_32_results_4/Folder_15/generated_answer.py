def return_binary_or_hexa(numbers):
    a, _, _, _, b = numbers[:5]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]