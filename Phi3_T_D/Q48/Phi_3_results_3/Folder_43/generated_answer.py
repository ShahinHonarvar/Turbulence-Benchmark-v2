def return_binary_or_hexa(numbers):
    try:
        a = numbers[10]
        b = numbers[28]
        missing_sum = sum(set(range(a + 1, b)).difference(numbers[10:29]))
        if not missing_sum:
            return ''
        if missing_sum & 1:
            return bin(missing_sum)[2:]
        return hex(missing_sum)[2:]
    except (IndexError, ValueError):
        raise ValueError('Function requires a tuple of nonnegative integers with at least 29 elements.')