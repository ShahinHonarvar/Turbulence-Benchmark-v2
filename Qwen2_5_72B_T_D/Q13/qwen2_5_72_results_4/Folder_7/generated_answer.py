def find_second_largest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    sliced_numbers = numbers[661:925]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)