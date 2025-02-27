def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 41:
        return None
    sliced_numbers = numbers[40:201]
    if len(sliced_numbers) < 2:
        return None
    first_smallest = min(sliced_numbers)
    sliced_numbers.remove(first_smallest)
    if not sliced_numbers:
        return None
    second_smallest = min(sliced_numbers)
    return second_smallest