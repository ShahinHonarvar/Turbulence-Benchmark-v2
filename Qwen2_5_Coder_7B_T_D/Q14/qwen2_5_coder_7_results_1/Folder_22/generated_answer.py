def find_second_smallest_num(numbers):
    sliced_numbers = numbers[40:201]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(set(sliced_numbers))
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None