def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 60:
        return None
    slice_numbers = numbers[59:98]
    if len(slice_numbers) < 2:
        return None
    slice_numbers.sort(reverse=True)
    return slice_numbers[1] if len(slice_numbers) > 1 else None