def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[35:50][1] if len(sorted_numbers) > 49 else None
    return second_smallest