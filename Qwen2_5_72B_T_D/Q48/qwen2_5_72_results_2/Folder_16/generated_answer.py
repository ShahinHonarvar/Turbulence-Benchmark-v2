def return_binary_or_hexa(numbers):
    if len(numbers) < 98 or not all((0 <= x <= numbers[97] for x in numbers[:97])):
        raise ValueError('Input must be a tuple of distinct nonnegative integers sorted in ascending order and have at least 98 elements.')
    a = numbers[90]
    b = numbers[97]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[91:97]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]