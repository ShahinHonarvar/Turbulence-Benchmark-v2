def find_second_smallest_num(numbers):
    sliced_numbers = numbers[19:93]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    second_smallest = sorted_numbers[1]
    return second_smallest