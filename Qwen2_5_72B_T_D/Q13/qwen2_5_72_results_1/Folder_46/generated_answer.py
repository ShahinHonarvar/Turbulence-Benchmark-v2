def find_second_largest_num(numbers):
    if len(numbers) < 88 or len(numbers) < 31:
        return None
    sliced_numbers = numbers[30:88]
    if len(sliced_numbers) < 2:
        return None
    max_num = max(sliced_numbers)
    sliced_numbers.remove(max_num)
    if not sliced_numbers:
        return None
    second_largest = max(sliced_numbers)
    return second_largest