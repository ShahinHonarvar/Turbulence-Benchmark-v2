def find_second_smallest_num(numbers):
    if len(numbers[4:-4]) < 2:
        return None
    sorted_range = sorted(numbers[4:-4])
    return sorted_range[1]