def find_second_largest_num(numbers):
    if len(numbers) < 101 or len(numbers) < 11:
        return None
    sliced_numbers = numbers[10:101]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]