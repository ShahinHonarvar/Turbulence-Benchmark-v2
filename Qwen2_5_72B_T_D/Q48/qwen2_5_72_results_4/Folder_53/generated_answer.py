def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[201:202]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]