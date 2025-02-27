def find_second_smallest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    sliced_numbers = numbers[660:925]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]