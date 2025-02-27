def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    total_sum = 0
    numbers_set = set(numbers[20:36])
    for num in range(a + 1, b):
        if num not in numbers_set:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]