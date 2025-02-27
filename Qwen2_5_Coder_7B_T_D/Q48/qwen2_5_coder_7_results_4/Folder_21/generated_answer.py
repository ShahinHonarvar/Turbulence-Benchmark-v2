def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[a + 1:b]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()