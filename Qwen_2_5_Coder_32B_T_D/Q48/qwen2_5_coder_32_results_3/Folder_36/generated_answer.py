def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    total_sum = 0
    present_numbers = set(numbers[110:349])
    for i in range(a + 1, b):
        if i not in present_numbers:
            total_sum += i
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]