def find_largest_num(numbers):
    start = 10
    end = 66
    return max(numbers[start:end + 1]) if start <= end else None