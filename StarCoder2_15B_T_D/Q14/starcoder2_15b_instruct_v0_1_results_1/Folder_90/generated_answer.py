def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 539:
        return sorted_numbers[528]
    else:
        return None