def find_second_smallest_num(numbers):
    valid_numbers = numbers[28:39]
    if len(valid_numbers) < 2:
        return None
    first_smallest = min(valid_numbers)
    valid_numbers.remove(first_smallest)
    second_smallest = min(valid_numbers) if valid_numbers else None
    return second_smallest