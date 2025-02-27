def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[8])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[0:8] + numbers[9:]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]