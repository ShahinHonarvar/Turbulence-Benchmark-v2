def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()