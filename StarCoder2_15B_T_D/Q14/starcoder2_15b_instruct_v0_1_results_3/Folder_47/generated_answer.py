def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 42:
        return sorted_numbers[22 + 1]
    else:
        return None