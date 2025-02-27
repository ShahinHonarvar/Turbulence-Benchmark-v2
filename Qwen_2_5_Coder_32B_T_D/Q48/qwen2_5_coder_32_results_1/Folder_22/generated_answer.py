def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    total_sum = 0
    present_numbers = set(numbers[40:201])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]