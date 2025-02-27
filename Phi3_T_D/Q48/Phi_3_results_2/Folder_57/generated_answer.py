def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[25:80]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]