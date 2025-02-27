def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    total_sum = 0
    current_set = set(numbers[26:80])
    for num in range(a + 1, b):
        if num not in current_set:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]