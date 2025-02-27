def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) >= 24:
        return sorted_numbers[23]
    else:
        return None