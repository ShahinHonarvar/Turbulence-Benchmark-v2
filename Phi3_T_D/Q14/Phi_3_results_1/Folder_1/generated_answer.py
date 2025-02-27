def find_second_smallest_num(numbers):
    if len(numbers) < 55 - 34 + 1:
        return None
    sorted_subset = sorted(numbers[34:56])
    return sorted_subset[1]