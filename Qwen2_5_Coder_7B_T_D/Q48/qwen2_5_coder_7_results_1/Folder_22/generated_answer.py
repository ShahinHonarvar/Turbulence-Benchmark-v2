def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    total = sum((i for i in range(a + 1, b) if i not in numbers[a + 1:b]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()