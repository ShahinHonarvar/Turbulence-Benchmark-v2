def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 30:
        return sorted_numbers[30]
    else:
        return None