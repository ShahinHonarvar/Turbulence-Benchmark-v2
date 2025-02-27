def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    total_sum = 0
    present_numbers = set(numbers[7:10])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]