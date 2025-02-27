def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 84 or len(numbers) < 70:
        return None
    sorted_slice = sorted(numbers[70:84 + 1])
    if len(sorted_slice) < 2:
        return None
    else:
        return sorted_slice[1]