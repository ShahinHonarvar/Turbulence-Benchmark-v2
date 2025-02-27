def find_second_largest_num(numbers):
    sliced_numbers = numbers[22:51]
    if len(sliced_numbers) < 2:
        return None
    sorted_slice = sorted(sliced_numbers, reverse=True)
    return sorted_slice[1] if sorted_slice else None