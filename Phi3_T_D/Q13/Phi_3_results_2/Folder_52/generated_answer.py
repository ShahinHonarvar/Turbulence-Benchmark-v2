def find_second_largest_num(numbers):
    if len(numbers) < 11 or 28 not in range(len(numbers)) or 38 not in range(len(numbers)):
        return None
    sorted_numbers = sorted(numbers[28:39])
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[-2]