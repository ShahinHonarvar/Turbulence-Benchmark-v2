def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    if len(sorted_numbers) >= 22:
        return sorted_numbers[20]
    else:
        return None