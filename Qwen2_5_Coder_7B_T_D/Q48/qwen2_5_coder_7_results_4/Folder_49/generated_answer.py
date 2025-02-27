def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in numbers[80:201]]
    total -= sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]