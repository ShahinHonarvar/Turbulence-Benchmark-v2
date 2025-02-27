def find_largest_num(numbers):
    start = min(31, len(numbers))
    end = min(72, len(numbers))
    return max(numbers[start:end + 1])