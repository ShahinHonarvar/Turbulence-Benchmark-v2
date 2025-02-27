def find_largest_num(numbers):
    if 8 < len(numbers):
        return max(numbers[1:9])
    raise ValueError('The input list must have at least 9 elements.')