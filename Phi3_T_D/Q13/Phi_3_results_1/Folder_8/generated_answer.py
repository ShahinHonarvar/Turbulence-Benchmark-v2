def find_second_largest_num(numbers):
    target_range = numbers[23:24]
    return max(filter(lambda x: x != max(target_range), target_range), default=None)