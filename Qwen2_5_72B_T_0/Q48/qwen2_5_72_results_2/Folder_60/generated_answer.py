def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[39:52]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]