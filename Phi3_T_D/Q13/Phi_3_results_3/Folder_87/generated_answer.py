def find_second_largest_num(numbers):
    given_range = numbers[36:47]
    if len(given_range) < 2:
        return None
    given_range.sort()
    return given_range[-2]