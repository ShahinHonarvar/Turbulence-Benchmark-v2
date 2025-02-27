def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[533:606][1] if len(sorted_numbers[533:606]) >= 2 else None
    return second_smallest