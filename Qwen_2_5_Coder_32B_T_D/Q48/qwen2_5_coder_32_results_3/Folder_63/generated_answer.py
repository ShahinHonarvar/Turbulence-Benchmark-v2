def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    target_sum = 0
    num_set = set(numbers[82:86])
    for num in range(a + 1, b):
        if num not in num_set:
            target_sum += num
    if target_sum == 0:
        return ''
    elif target_sum % 2 == 1:
        return bin(target_sum)[2:]
    else:
        return hex(target_sum)[2:]