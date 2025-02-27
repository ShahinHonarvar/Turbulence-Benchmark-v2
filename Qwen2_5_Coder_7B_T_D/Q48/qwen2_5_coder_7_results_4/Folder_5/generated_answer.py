def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in numbers[a + 1:b]]
    total -= sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()