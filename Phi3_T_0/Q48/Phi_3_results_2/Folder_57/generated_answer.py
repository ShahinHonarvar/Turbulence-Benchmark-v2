def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[25:81]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]