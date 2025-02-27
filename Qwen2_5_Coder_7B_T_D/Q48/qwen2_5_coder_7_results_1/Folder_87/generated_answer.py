def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    total = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[a + 1:b]]
    total -= sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]