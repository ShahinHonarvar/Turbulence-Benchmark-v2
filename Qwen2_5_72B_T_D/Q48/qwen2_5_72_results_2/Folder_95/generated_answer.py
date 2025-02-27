def return_binary_or_hexa(numbers):
    if len(numbers) < 100 or not all((isinstance(x, int) and x >= 0 for x in numbers)):
        raise ValueError('Invalid input. The argument must be a tuple of at least 100 distinct nonnegative integers.')
    a = numbers[32]
    b = numbers[99]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]