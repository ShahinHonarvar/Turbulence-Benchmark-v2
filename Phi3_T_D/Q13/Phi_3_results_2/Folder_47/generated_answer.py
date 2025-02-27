def find_second_largest_num(numbers):
    if len(numbers) < 38:
        return None
    sliced_numbers = numbers[37:77]
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]