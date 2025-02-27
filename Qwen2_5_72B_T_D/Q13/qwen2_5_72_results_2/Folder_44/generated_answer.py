def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sliced_numbers = numbers[12:68]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)