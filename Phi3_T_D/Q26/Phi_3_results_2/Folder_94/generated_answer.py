def sum_in_range(numbers):
    result = sum((x for x in numbers if 36 <= x <= 52))
    return result if result > 0 else 0