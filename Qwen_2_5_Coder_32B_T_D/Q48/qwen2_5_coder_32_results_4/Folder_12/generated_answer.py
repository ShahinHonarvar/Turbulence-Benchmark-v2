def return_binary_or_hexa(numbers):
    a, b = (numbers[16], numbers[87])
    total_sum = 0
    numbers_set = set(numbers[16:88])
    for num in range(a + 1, b):
        if num not in numbers_set:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]