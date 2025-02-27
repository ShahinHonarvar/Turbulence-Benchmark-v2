def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[a:b + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]