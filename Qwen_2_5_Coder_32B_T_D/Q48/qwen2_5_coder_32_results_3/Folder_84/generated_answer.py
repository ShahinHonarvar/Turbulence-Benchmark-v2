def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    total_sum = 0
    nums_set = set(numbers[32:45])
    for num in range(a + 1, b):
        if num not in nums_set:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]