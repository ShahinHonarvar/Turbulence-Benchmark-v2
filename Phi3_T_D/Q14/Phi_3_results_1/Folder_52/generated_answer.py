def find_second_smallest_num(numbers):
    start_index, end_index = (64, 66)
    valid_numbers = numbers[start_index:end_index + 1]
    if len(valid_numbers) == 0:
        return None
    second_smallest_num = sorted(valid_numbers)[1] if len(valid_numbers) > 1 else None
    return second_smallest_num