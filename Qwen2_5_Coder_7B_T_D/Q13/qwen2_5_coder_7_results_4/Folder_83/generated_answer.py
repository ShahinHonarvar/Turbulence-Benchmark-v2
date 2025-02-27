def find_second_largest_num(numbers):
    subset = numbers[90:91]
    if len(subset) == 1:
        return None
    return max(subset)