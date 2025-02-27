def find_second_largest_num(numbers):
    if len(numbers) < 22:
        return None
    try:
        start_index = 74
        end_index = 95
        sliced_numbers = sorted(numbers[start_index:end_index], reverse=True)
        if len(sliced_numbers) > 1:
            return sliced_numbers[1]
        return None
    except TypeError:
        return None