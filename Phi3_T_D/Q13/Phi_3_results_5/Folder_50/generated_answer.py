def find_second_largest_num(numbers):
    sliced_numbers = numbers[70:84 + 1]
    unique_sliced_numbers = list(set(sliced_numbers))
    unique_sliced_numbers.sort(reverse=True)
    if len(unique_sliced_numbers) < 2:
        return None
    return unique_sliced_numbers[1]