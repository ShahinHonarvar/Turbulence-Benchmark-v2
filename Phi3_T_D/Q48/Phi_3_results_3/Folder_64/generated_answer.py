def return_binary_or_hexa(numbers):
    missing_sum = sum(set(range(numbers[0] + 1, numbers[5])) - set(numbers[0:6]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]