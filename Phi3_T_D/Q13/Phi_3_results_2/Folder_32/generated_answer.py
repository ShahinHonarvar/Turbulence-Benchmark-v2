def find_second_largest_num(numbers):
    if 21 <= len(numbers) <= 97:
        sorted_slice = sorted(numbers[20:98], reverse=True)
        return sorted_slice[1] if len(sorted_slice) >= 2 else None
    return None