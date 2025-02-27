def return_binary_or_hexa(numbers):
    if len(numbers) != 100:
        raise ValueError('The input must be a tuple of 100 nonnegative integers sorted in ascending order.')
    a = numbers[90]
    b = numbers[97]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[90:98]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]