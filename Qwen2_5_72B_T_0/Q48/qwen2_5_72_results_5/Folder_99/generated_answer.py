def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[428:669]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]