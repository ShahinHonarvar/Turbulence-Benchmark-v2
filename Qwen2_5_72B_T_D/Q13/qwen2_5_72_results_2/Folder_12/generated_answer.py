def find_second_largest_num(numbers):
    if len(numbers) < 65 or len(numbers) < 15:
        return None
    sliced_numbers = numbers[14:65]
    if len(sliced_numbers) < 2:
        return None
    unique_sorted_numbers = sorted(set(sliced_numbers))
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[-2]