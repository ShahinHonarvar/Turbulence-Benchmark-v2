def find_second_smallest_num(numbers):
    sliced_numbers = numbers[28:33]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]