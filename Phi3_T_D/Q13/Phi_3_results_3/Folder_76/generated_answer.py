def find_second_largest_num(numbers):
    if 686 >= len(numbers) or 987 < 686:
        return None
    sliced_numbers = numbers[686:988]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)