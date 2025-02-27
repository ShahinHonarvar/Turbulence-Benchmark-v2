def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    present_numbers = set(numbers[11:77])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present_numbers:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]