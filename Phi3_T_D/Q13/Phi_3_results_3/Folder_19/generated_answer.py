def find_second_largest_num(numbers):
    if len(numbers) < 6 or not 3 <= len(numbers) <= 5:
        return None
    sorted_slice = sorted(numbers[3:6], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None