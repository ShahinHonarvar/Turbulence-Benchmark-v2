def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    num_set = set(numbers)
    total_sum = 0
    for num in range(a + 1, b):
        if num not in num_set:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]