def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    total = sum(range(a + 1, b))
    for num in numbers[33:99]:
        total -= num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]