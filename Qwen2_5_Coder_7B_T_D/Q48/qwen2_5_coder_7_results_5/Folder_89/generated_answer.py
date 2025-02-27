def return_binary_or_hexa(numbers):
    a, b = (numbers[55], numbers[84])
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()