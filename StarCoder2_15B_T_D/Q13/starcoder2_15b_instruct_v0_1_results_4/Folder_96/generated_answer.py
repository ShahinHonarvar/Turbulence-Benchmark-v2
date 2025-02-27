def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = sorted_numbers[1] if len(sorted_numbers) >= 2 else None
    return second_largest