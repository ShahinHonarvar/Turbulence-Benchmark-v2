def find_second_largest_num(numbers):
    sliced_numbers = numbers[52:72]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)