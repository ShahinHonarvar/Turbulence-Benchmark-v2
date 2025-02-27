def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    total_sum = 0
    present_numbers = set(numbers[52:76])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]