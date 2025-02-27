def return_binary_or_hexa(numbers):
    a, b = (numbers[3], numbers[8])
    total_sum = 0
    given_set = set(numbers[3:9])
    for num in range(a + 1, b):
        if num not in given_set:
            total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]