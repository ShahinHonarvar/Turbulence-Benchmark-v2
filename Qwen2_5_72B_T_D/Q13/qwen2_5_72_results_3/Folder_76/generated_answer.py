def find_second_largest_num(numbers):
    if len(numbers) < 987 or len(numbers) < 686:
        return None
    sliced_numbers = numbers[686:988]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]