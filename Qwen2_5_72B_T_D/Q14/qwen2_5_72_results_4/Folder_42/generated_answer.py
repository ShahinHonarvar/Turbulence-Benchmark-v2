def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(set(numbers[21:98])) < 2:
        return None
    sorted_slice = sorted(numbers[21:98])
    return sorted_slice[1]