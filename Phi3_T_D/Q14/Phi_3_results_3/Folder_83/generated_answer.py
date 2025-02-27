def find_second_smallest_num(numbers):
    subset = sorted(numbers[90:201])
    if len(subset) < 2:
        return None
    distinct_numbers = sorted(set(subset))
    return distinct_numbers[1] if len(distinct_numbers) > 1 else None