def find_second_smallest_num(numbers):
    if not 59 <= len(numbers) <= 97:
        return None
    sorted_subset = sorted(numbers[59:98])
    unique_numbers = {n for n in sorted_subset}
    if len(unique_numbers) < 2:
        return None
    return next(iter(unique_numbers))