def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) < 37:
        return None
    second_smallest = sorted_numbers[36]
    return second_smallest