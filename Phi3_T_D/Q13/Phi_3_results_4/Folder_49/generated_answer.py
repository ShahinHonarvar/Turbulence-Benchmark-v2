def find_second_largest_num(numbers):
    start_index = min(80, len(numbers))
    end_index = min(200, len(numbers))
    sorted_slice = sorted(numbers[start_index:end_index], reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]