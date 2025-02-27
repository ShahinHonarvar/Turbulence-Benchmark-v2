def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    sum_ab = sum(range(a + 1, b)) - sum(numbers[a + 1:b])
    return bin(sum_ab)[2:] if sum_ab % 2 else str(hex(sum_ab))[2:]