def find_second_largest_num(numbers):
    numbers_sorted = sorted(set(numbers), reverse=True)
    return numbers_sorted[1] if len(numbers_sorted) > 1 else None