def find_second_smallest_num(numbers):
    start_index = 74
    end_index = 95
    if start_index >= end_index or not (start_index <= len(numbers) and end_index <= len(numbers)):
        return None
    sorted_slice = sorted(numbers[start_index:end_index + 1])
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None