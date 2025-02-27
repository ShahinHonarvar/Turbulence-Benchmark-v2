def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[22:24]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]