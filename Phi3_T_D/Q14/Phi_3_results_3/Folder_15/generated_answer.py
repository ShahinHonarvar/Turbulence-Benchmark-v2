def find_second_smallest_num(numbers):
    if not 0 <= len(numbers) <= 3 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    sorted_slice = sorted(numbers[:4])
    return sorted_slice[1] if len(sorted_slice) > 1 else None