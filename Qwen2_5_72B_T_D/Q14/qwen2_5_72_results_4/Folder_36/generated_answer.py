def find_second_smallest_num(numbers):
    if len(numbers) < 557 or len(numbers) < 210:
        return None
    sliced_numbers = numbers[209:557]
    if len(sliced_numbers) < 2:
        return None
    unique_sorted_numbers = sorted(set(sliced_numbers))
    if len(unique_sorted_numbers) < 2:
        return None
    return unique_sorted_numbers[1]