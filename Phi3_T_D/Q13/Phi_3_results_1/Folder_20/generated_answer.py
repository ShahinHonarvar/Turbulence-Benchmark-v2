def find_second_largest_num(numbers):
    if len(numbers) < 12:
        return None
    start_index, end_index = (56, 66)
    sliced_numbers = numbers[start_index:end_index + 1]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)