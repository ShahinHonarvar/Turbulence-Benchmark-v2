def find_largest_num(numbers):
    if len(numbers) < 79:
        return 'Index out of range'
    return max(numbers[17:79])