def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[43:71]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()