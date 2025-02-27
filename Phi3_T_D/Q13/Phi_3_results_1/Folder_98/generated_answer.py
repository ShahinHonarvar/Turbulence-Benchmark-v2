def find_second_largest_num(numbers):
    if len(numbers) > 6:
        numbers = numbers[:7]
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1] if sorted_numbers[1] is not None else None