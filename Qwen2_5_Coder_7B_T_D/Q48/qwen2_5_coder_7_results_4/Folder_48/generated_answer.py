def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]