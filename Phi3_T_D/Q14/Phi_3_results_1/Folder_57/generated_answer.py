def find_second_smallest_num(numbers):
    if len(numbers) < 11 or numbers[20:31] == []:
        return None
    sorted_slice = sorted(numbers[20:31])
    return sorted_slice[1] if len(sorted_slice) > 1 else None