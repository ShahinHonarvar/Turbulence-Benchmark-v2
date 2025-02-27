def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[2:4]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]