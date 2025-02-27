def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) >= 26:
        return sorted_numbers[25]
    else:
        return None