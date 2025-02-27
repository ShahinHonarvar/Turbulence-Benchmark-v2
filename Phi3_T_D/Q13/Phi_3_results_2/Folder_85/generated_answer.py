def find_second_largest_num(numbers):
    if len(numbers[6:11]) < 2:
        return None
    sorted_slice = sorted(numbers[6:11], reverse=True)
    return sorted_slice[1] if sorted_slice[1] != sorted_slice[0] else None