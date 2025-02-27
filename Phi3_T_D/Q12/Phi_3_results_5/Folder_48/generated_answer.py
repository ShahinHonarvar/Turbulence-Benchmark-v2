def find_smallest_num(numbers):
    start = min(len(numbers), 209)
    end = min(556, len(numbers))
    return min(numbers[start:end + 1])