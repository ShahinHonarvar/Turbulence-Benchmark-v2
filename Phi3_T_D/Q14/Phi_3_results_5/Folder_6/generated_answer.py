def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) > 51:
        return None
    sorted_slice = sorted(numbers[29:80])
    return sorted_slice[1] if len(sorted_slice) > 1 else None