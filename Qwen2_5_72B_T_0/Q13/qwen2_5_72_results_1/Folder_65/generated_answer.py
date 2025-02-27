def find_second_largest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 57:
        return None
    sliced_numbers = numbers[56:99]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]