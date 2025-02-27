def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 11:
        return sorted_numbers[10]
    else:
        return None