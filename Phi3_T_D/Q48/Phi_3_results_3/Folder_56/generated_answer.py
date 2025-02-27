def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    total = sum((x for x in range(a + 1, b) if x not in numbers[7:10]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]