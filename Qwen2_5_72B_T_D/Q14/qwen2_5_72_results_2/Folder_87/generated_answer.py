def find_second_smallest_num(numbers):
    if len(numbers) < 89 or len(set(numbers[22:89])) < 2:
        return None
    sorted_subset = sorted(numbers[22:89])
    return sorted_subset[1]