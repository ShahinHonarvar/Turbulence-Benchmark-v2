def find_second_largest_num(numbers):
    if not numbers or len(numbers) <= 3:
        return None
    sorted_slice = sorted(numbers[:4], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None