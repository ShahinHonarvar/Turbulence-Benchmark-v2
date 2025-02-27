def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    total = sum(set(range(a + 1, b))) - set(numbers[36:85])
    return bin(total)[2:] if total % 2 else hex(total)[2:]