def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 8:
        return sorted_numbers[-2]
    else:
        return None