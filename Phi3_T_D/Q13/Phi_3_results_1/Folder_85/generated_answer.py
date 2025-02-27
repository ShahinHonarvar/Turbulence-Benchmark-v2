def find_second_largest_num(numbers):
    start_index = 6
    end_index = 8
    sorted_slice = sorted(numbers[start_index:end_index + 1], reverse=True)
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    return None