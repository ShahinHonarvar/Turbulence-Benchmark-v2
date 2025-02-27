def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[34:56], reverse=True)
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]
    return None