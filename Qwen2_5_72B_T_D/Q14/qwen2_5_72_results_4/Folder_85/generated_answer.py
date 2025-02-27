def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    numbers_subset = numbers[:7]
    numbers_subset.sort()
    return numbers_subset[1] if len(numbers_subset) > 1 else None