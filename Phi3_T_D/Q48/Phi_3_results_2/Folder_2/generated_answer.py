def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    total = sum((i for i in range(a + 1, b) if i not in numbers[72:93]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]