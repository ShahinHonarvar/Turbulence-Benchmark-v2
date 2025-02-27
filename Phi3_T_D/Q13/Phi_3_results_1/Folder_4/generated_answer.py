def find_second_largest_num(numbers):
    sliced_numbers = numbers[12:93]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers, reverse=True)
    return sorted_numbers[1]