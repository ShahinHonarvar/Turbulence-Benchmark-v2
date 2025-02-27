def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers_filtered = numbers[56:58]
    if len(numbers_filtered) < 2:
        return None
    first_largest = max(numbers_filtered)
    numbers_filtered.remove(first_largest)
    second_largest = max(numbers_filtered) if numbers_filtered else None
    return second_largest