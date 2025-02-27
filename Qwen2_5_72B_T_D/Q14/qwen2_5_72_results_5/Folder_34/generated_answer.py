def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) > 201 or len(set(numbers[60:201])) < 2:
        return None
    sliced_numbers = numbers[60:201]
    min_num = min(sliced_numbers)
    sliced_numbers.remove(min_num)
    second_min_num = min(sliced_numbers)
    return second_min_num