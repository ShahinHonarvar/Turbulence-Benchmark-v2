def find_second_largest_num(numbers):
    return sorted(numbers[19:93], reverse=True)[1] if len(numbers[19:93]) > 1 else None