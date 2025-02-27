def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[82:87][1] if len(sorted_numbers) >= 87 else None
    return second_smallest