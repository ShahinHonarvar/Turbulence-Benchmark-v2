def find_second_smallest_num(numbers):
    if 22 <= len(numbers) <= 63:
        sorted_slice = sorted(numbers[22:64])
        return sorted_slice[1] if len(sorted_slice) > 1 else None
    else:
        return None