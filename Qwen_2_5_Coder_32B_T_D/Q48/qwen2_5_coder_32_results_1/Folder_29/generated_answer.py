def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    total_sum = 0
    present_numbers = set(numbers[70:99])
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()