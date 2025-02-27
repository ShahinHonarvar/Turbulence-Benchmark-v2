def find_second_smallest_num(numbers):
    if len(numbers) < 29:
        return None
    sorted_slice = sorted(numbers[22:51])
    return sorted_slice[1] if len(sorted_slice) > 1 else None