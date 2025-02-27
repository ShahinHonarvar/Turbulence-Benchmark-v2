def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[14:70]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]