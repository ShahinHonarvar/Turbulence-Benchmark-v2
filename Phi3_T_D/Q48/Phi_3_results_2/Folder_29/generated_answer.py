def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[70:99]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]