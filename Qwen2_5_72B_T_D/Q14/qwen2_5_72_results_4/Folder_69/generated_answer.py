def find_second_smallest_num(numbers):
    if len(numbers) < 88 or len(set(numbers[25:88])) < 2:
        return None
    sorted_slice = sorted(numbers[25:88])
    return sorted_slice[1]