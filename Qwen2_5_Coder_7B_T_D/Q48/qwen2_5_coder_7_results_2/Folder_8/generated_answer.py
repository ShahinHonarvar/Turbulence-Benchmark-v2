def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    total = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[45:49]]
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()