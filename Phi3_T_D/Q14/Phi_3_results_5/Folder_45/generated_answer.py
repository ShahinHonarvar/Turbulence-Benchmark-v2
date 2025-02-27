def find_second_smallest_num(numbers):
    range_numbers = numbers[30:201]
    if len(range_numbers) < 2:
        return None
    second_smallest = min(range_numbers)
    for num in range_numbers:
        if num > second_smallest:
            return num
    return None