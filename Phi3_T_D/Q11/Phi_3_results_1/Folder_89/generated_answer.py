def find_largest_num(numbers):
    if len(numbers) >= 82:
        return max(numbers[56:83])
    raise IndexError('List does not contain enough elements.')