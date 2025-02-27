def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[74:84]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]