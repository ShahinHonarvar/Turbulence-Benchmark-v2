def find_second_smallest_num(numbers):
    start_idx, end_idx = (75, 85)
    slice_of_numbers = numbers[start_idx:end_idx + 1]
    if len(slice_of_numbers) < 2:
        return None
    second_smallest = sorted(slice_of_numbers)[1]
    return second_smallest