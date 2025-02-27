def find_second_largest_num(numbers):
    if len(numbers) < 19 or len(numbers[30:49]) < 2:
        return None
    sorted_slice = sorted(numbers[30:49], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else sorted_slice[0]