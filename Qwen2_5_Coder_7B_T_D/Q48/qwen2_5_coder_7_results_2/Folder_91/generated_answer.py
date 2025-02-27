def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[6]
    total = sum(range(a + 1, b)) - sum((numbers[i] for i in range(1, 6)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()