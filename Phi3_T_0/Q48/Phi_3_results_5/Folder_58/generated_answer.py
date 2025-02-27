def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[275:872]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]