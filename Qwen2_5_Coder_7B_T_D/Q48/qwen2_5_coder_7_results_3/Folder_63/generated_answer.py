def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[81:87]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()