def find_second_largest_num(numbers):
    if len(numbers) < 44:
        return None
    sorted_numbers = sorted(numbers[43:87], reverse=True)
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]
    return None